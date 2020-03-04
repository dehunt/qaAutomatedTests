import logging, os, configparser, sys, argparse
from src import reporting, prep, product, version, netdrive, installers, uninstallers
from pathlib import Path

# Note for updating GUI handling with pywinauto. These two functions are useful for finding elements:
#       .print_control_identifiers()
#       .draw_outline()

# Setup reportdir and fetch config.cfg settings
reportdir = prep.create_dir(os.path.join(prep.get_directory(), "reports"))
config = configparser.ConfigParser()
config.read('config.cfg')

# Setup Logging
logger = logging.getLogger('qaAutomatedTesting')
logger.setLevel(logging.DEBUG)
# debug file handler
dfh = logging.FileHandler(os.path.join(reportdir, reporting.get_debug_filename()))
dfh.setLevel(logging.DEBUG)
dfh.setFormatter(logging.Formatter(config['LOGGER']['verbose'], config['LOGGER']['timeformat']))
# 'report' file handler (separate file demo)
        # rfh = logging.FileHandler(os.path.join(reportdir, reporting.get_report_filename()))
        # rfh.setLevel(logging.INFO)
        # rfh.setFormatter(logging.Formatter(config['LOGGER']['reportformat'], config['LOGGER']['timeformat']))
        # console output file handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter(config['LOGGER']['simple'], config['LOGGER']['timeformat']))
logger.addHandler(dfh)
# logger.addHandler(rfh)
logger.addHandler(ch)

# Create Prep class. This is common throughout the script. It's done this way to accommodate logger reporting.
#    This way lets the logger output tag itself with the associated class
Prep = prep.Prep()
# Get platform this script is running on
platform = Prep.verify_platform()

# If windows, check if admin. Admin is required because the script can install / remove programs
#   Potential change: Allow non-admin, but stop and report why if user attempts to install / uninstall program w/script
if platform == "Windows":
    if prep.is_admin():
        logger.debug("Script run as admin")
    else:
        logger.debug("Script not run as admin")
        logger.info("Script must be run as administrator.")
        sys.exit()

# Verify / Setup installation class
Prod = product.Product()
# Version class
Ver = version.Version()

# ArgParse handling
logger.debug("Starting argument parser")
parser = argparse.ArgumentParser(description="qaAutomatedTest Framework")
parser.add_argument('-p', '--product', help='should be one of: alch, checker, optimizer', default=False)
parser.add_argument('-v', '--version', help='varies by product.   alch/checker/optimizer is x.x.x,   apdfl will be PXy', default=False)
parser.add_argument('-s', '--state', help='should be one of: "pending" or "approved"', default=False)
args = parser.parse_args()
# Verify product argument if it exists. If invalid or doesn't exist, get product from user.
if args.product is not False:
    prod_check = Prod.verify_product_arg_input(args.product)
    if prod_check is False:
        product = Prod.get_user_product_input()
    else:
        product = args.product
else:
    product = Prod.get_user_product_input()
# Verify version argument if it exists. If invalid or doesn't exist, get version from user.
if args.version is not False:
    version_check = Ver.verify_version_arg_input(product, args.version)
    if version_check is False:
        version = Ver.get_version_from_user(product)
    else:
        version = args.version
else:
    version = Ver.get_version_from_user(product)
# Get approved / pending product state, or set to False. This will be handled later.
if args.state is not False:
    release_state = args.state
else:
    release_state = False

# Generate the default exe name. Derived from product and platform
config_exe = config['EXECUTABLES']
exe_name = Prod.get_exe_name(product, platform, config_exe)
logger.debug("Generated exe_name: " + exe_name)

# Check for an existing installation for PRODUCT. Install loc checked is in config[INSTALL]. Varies by product.
# If it exists, check if user wants to use it, or reinstall. Otherwise, install new version.
App = installers.AppSetup()
install_loc = App.get_default_install_loc(platform, product, config['INSTALL'])

run_install = False   # Expects variable to be False, except if it should install the product
currently_exists = App.check_for_existing_installation(install_loc, exe_name)
if currently_exists == True:
    query_use_existing_install = App.use_existing()
    if query_use_existing_install == True:
        logger.info("Using existing version")
    if query_use_existing_install == False:
        AppUninstaller = uninstallers.AppUninstall()
        AppUninstaller.uninstall_product(product, platform, install_loc, config['UNINSTALLER'])
        run_install = True
else:
    run_install = True

if run_install == True:
    logger.debug("Running install logic")
    # Build installation file name
    InstFile = netdrive.InstallFile()
    installer_name = InstFile.build_product_installer_name(product, version, platform, config['INSTALLBASENAME'])
    installer_loc = InstFile.build_product_install_loc(product, platform, config['NETDRIVE'], release_state, version)

    # Fetch installation file
    Net = netdrive.Network()
    Net.get_release_from_network(os.path.join(installer_loc, installer_name), platform)

    # Set install target loc (used only for linux currently)
    # Should expand in future to let script set install loc during windows install
    install_target_loc = config['INSTALL']['d_' + product + '_lin_install']
    logger.debug("install_target_loc is: "+install_target_loc)

    # Run installation file
    App.run_product_installation(platform, product, os.path.join(prep.get_directory(), "installers", installer_name), install_target_loc)

# Build exe path + command using default install location
if platform == "Windows":
    exe = Path(config['INSTALL']['d_' + product + '_win_install']) / exe_name
if platform == "Linux":
    exe = Path(config['INSTALL']['d_' + product + '_lin_install']) / exe_name
logger.debug("Exe is: " + str(exe) + " for product " + product)

Report = reporting.Reporting()
if product == "alch":
    from tests_alchemist import alchMain
    Report.report("Beginning PDF Alchemist Automated Test for " + str(platform) + " v" + str(version))
    test = alchMain.AlchemistTest()
if product == 'checker':
    from tests_checker import checkerMain
    Report.report("Beginning PDF Checker Automated Test for " + str(platform) + " v" + str(version))
    test = checkerMain.CheckerTest()
if product == 'optimizer':
    from tests_optimizer import optimizerMain
    Report.report("Beginning PDF Optimizer Automated Test for " + str(platform) + " v" + str(version))
    test = optimizerMain.OptimizerTest()

test.pytest_session_start()
test.pytest_run_test(exe, platform)
test.pytest_session_finish()