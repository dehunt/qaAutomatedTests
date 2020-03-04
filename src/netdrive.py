import os, logging, sys, shutil, warnings
# from pathlib import Path, PureWindowsPath
from src.prep import create_dir, get_directory
# from shutil import copyfile

log = logging.getLogger('qaAutomatedTesting')
warnings.simplefilter('ignore', category=UserWarning) # filters out the 32b / 64b app warning from pywinauto

class InstallFile:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.InstallFile')
        self.logger.debug('Creating an instance of InstallFile')

    # Build the product installation name. This is the product installed that will be retrieved from the network drive
    # Returns product installer file name.
    def build_product_installer_name(self, product, version, platform, config, lm_flag=None):
        plat_switch = {
            "Windows": "Win64",
            "Linux": "Linux64"
        }
        prod_extension_switch = {
            "Windows": ".exe",
            "Linux": ".bsx"
        }
        self.logger.debug("Beginning build product name")
        if lm_flag is not None:
            self.logger.critical("lm_flag is not None")
            print("LM not implemented - how did you get here?")
            sys.exit()
        else:
            s = plat_switch.get(platform, "Invalid platform")
            self.logger.debug("build_product_installer_name platform switcher returning " + str(s))
            e = prod_extension_switch.get(platform, "Invalid platform")
            self.logger.debug("build_product_installer_name extension switcher returning " + str(e))
            if product == 'apdfl':
                print("not implemented")
                self.logger.debug("Unsupported product selected: " + product)
                sys.exit()
            if product == 'flip2pdf':
                print("not implemented")
                self.logger.debug("Unsupported product selected: " + product)
                sys.exit()
            n = config['i_'+ product + '_base'] + str(s) + "_" + str(version) + str(e)
            return n

    # Build the product installer location. This is the location of the installer on the network drive
    # Returns fully built installer location path
    def build_product_install_loc(self, product, platform, config, release_state, version):
        self.logger.debug("Building install loc with product " + str(product) + ", platform " + str(platform))
        if platform == "Windows":
            baseloc = config['winReleases']
            if product == "checker": plt_loc = "Windows64"
            else: plt_loc = "Win64"
        elif platform == "Linux":
            baseloc = config['linReleases']
            plt_loc = "Linux64"
        else:
            self.logger.critical("Platform not found: " + platform)
            sys.exit()
        if product == "alch":
            prod_loc = "PDFAlchemist"
        elif product == "checker":
            prod_loc = "PDFChecker"
            v_name = config['checker_v_name'] + ".".join(version.split(".")[:2])
        elif product == "optimizer":
            prod_loc = "PDFOptimizer"
            v_name = config['optimizer_v_name'] + ".".join(version.split(".")[:2])
        else:
            self.logger.critical("Product not found " + product)
            sys.exit()
        if 'v_name' in locals():
            r = os.path.join(baseloc, prod_loc, plt_loc, v_name)
        else:
            r = os.path.join(baseloc, prod_loc, plt_loc)
        if release_state is not False:
            self.logger.debug("Verifying release_state argument for product: " + str(release_state))
            state_list = ['approved', 'pending']
            if not any(release_state in s for s in state_list):
                release_state = self.get_release_state_from_user(r)
        else:
            release_state = self.get_release_state_from_user(r)
        r = self.append_release_state_path(r, product, release_state)
        self.logger.debug("Built: " + str(r))
        return r

    # Appends the release state path to the installer location path, then returns the path.
    # r = installer path up to this point.
    # Returns updated installer path
    def append_release_state_path(self, r, product, release_state):
        if (release_state == 'approved') and (product == 'alch'):
            r = os.path.join(r, "approved", "current")
        elif (release_state == 'approved') and ((product == 'checker') or (product == 'optimizer')):
            r = os.path.join(r, "current", "standard")
        elif release_state == 'pending':
            r = os.path.join(r, "pending")
        else:
            self.logger.critical("Failed to build r path")
            sys.exit()
        return r

    # Gets approved or pending from the user.
    # Expected return: "approved" or "pending"
    def get_release_state_from_user(self, path):
        print("Use approved or pending version?")
        print("    1: Approved")
        print("    2: Pending")
        print("    9: Cancel")
        uin = input("--> ")
        self.logger.debug('Approved/Pending input received is: ' + str(uin))
        if uin == '9':
            print("Exiting")
            sys.exit()
        if (uin != '1') and (uin != '2') and (uin != 9):
            self.logger.debug("Invalid input: " + uin)
            self.logger.info("Invalid input. Exiting.")
            sys.exit()
        if (uin == '1'):
            ret = 'approved'
        if (uin == '2'):
            ret = 'pending'
        return ret

class Network:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Network')
        self.logger.debug('Creating an instance of Network')
    # Fetches the release installation file from the appropriate network drive
    def get_release_from_network(self, installer, platform):
        self.logger.debug("Verifying installers directory at: " + os.path.join(get_directory(), "installers"))
        create_dir(os.path.join(get_directory(), "installers"))
        if os.path.isfile(installer):
            if platform == "Windows":
                try:
                    self.logger.debug("Transfering file for windows: " + installer)
                    shutil.copy(installer, os.path.join(get_directory(), "installers"))
                except WindowsError as e:
                    self.logger.critical("ERROR: WINDOWSERROR = ", e)
                    print("ERROR: WINDOWSERROR = ", e)
                except:
                    self.logger.critical("ERROR: Some other error happened")
            if platform == "Linux":
                try:
                    self.logger.debug("Transfering file for linux: " + installer)
                    shutil.copy(installer, os.path.join(get_directory(), "installers"))
                except:
                    self.logger.critical("ERROR: Some other error happened")
        else:
            self.logger.critical("ERROR: File not found: " + installer)
            sys.exit()
        # if platform == "Windows":
        #     if os.path.isfile(installer):
        #         try:
        #             shutil.copy(installer, os.path.join(get_directory(), "installers"))
        #         except WindowsError as e:
        #             self.logger.critical("ERROR: WINDOWSERROR = ", e)
        #             print("ERROR: WINDOWSERROR = ", e)
        #         except:
        #             self.logger.critical("ERROR: Some other error happened")
        #     else:
        #         self.logger.critical("ERROR: File not found: " + installer)
        #         sys.exit()
        #