import os, logging, sys
from time import sleep

class AppSetup:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.AppSetup')
        self.logger.debug('Creating an instance of AppSetup')

    # Return true if the exe file is found here
    def check_for_existing_installation(self, default_install_loc, exe_name):
        current_install = os.path.join(default_install_loc, exe_name)
        self.logger.debug('Checking for current install at ' + current_install)
        is_found = os.path.isfile(current_install)
        self.logger.debug('Returning: ' + str(is_found))
        return is_found

    # Queries user to check if script should proceed with the located version, or to uninstall and reinstall
    # Returns true if script should use current, and false if script should uninstall then reinstall
    def use_existing(self):
        s = '0'
        self.logger.debug("Getting user input on install (1), uninstall (2), or cancel and exit (9)")
        while s == '0':
            print("Existing installation found.")
            print("   1: Use this version")
            print("   2: Uninstall this version")
            print("   9: Cancel")
            s = input("--> ")
        self.logger.debug('Input received is: ' + str(s))
        if s == '9':
            print("Exiting")
            sys.exit()
        if s == '1':
            return True
        if s == '2':
            return False
        else:
            print("Invalid return. Exiting.")
            self.logger.debug("Invalid return")
            sys.exit()

    # Builds the default install location for product by platform.
    # Returns the default install location.
    def get_default_install_loc(self, platform, product, config):
        if platform == "Windows":
            install_loc = config['d_'+product+'_win_install']
        if platform == "Linux":
            install_loc = config['d_' + product + '_lin_install']
        self.logger.debug("Returning install loc for " + platform + " " + product + ": " + install_loc)
        return install_loc

    # Installs the product by calling the appropriate installer function.
    # This will use pywinauto for the GUI on windows, or Popen on linux.
    def run_product_installation(self, platform, product, product_installer, install_target_loc):
        self.logger.debug("Install target loc for " + product + " " + platform + " is: " + install_target_loc)
        if product == "alch":
            self.run_alchemist_product_installation(platform, product_installer, install_target_loc)
        elif product == "checker":
            self.run_checker_product_installation(platform, product_installer, install_target_loc)
        elif product == "optimizer":
            self.run_optimizer_product_installation(platform, product_installer, install_target_loc)
        else:
            self.logger.critical("No product logic found for " + product)
            sys.exit()

    def run_alchemist_product_installation(self, platform, product_installer, install_target_loc):
        self.logger.debug("   Installing alchemist for platform: " + platform)
        self.logger.debug("   Installer is: " + str(product_installer))
        if platform == "Windows":
            import pywinauto
            app = pywinauto.Application(backend="win32").start(product_installer)
            sleep(2)
            app = pywinauto.Application().connect(title_re="Setup - PDF Alchemist.*", visible_only="True")
            pywinauto.timings.Timings.slow()
            if app.PDF_Alchemist_Premium.Next.exists():
                app.PDF_Alchemist_Premium.Next.click()
            app.PDF_Alchemist_Premium.Install.click()
            app.PDF_Alchemist_Premium.Finish.click()
        if platform == "Linux":
            from subprocess import Popen, PIPE
            p = Popen(product_installer, stdin=PIPE, shell=True)
            # encode string to bytes for p.communicate()
            target = (install_target_loc + '\n').encode('utf-8')
            p.communicate(input=target)
        self.logger.debug("   Installer complete")

    # On windows, worth through the GUI while agreeing to the EULA and unchecking the optimizer install option
    def run_checker_product_installation(self, platform, product_installer, install_target_loc):
        self.logger.debug("   Installing checker for platform: " + platform)
        self.logger.debug("   Installer is: " + str(product_installer))
        if platform == "Windows":
            import pywinauto
            app = pywinauto.Application(backend="uia").start(product_installer)
            sleep(2)
            app = pywinauto.Application().connect(title_re="Setup - PDF Checker", visible_only="True")
            pywinauto.timings.Timings.slow()
            app.PDF_Checker.I_accept_the_agreement.click()
            app.PDF_Checker.Next.click()
            app.PDF_Checker.Next.click()
            app.PDF_Checker.TNewCheckListBox.click()
            app.PDF_Checker.Next.click()
            app.PDF_Checker.Install.click()
            app.PDF_Checker.Finish.click()

        # Linux install. p.communicate is used to accept the EULA. Popen is opened with home as the cwd.
        # To-do: Pass multiple communicates in a way that: accepts EULA, inputs install directory, declines optimizer
        if platform == "Linux":
            from subprocess import Popen, PIPE
            from . import prep as prep
            prep.create_dir(install_target_loc)
            p = Popen(product_installer, cwd=str(os.path.dirname(install_target_loc)), stdin=PIPE, shell=True)
            # encode string to bytes for p.communicate()
            p.communicate(input='y'.encode('utf-8'))
        self.logger.debug("   Installer complete")

    def run_optimizer_product_installation(self, platform, product_installer, install_target_loc):
        self.logger.debug("   Installing optimizer for platform: " + platform)
        self.logger.debug("   Installer is: " + str(product_installer))
        if platform == "Windows":
            import pywinauto
            app = pywinauto.Application(backend="uia").start(product_installer)
            sleep(2)
            app = pywinauto.Application().connect(title_re="Setup - PDF Optimizer", visible_only="True")
            pywinauto.timings.Timings.slow()
            app.PDF_Optimizer.I_accept_the_agreement.click()
            app.PDF_Optimizer.Next.click()
            app.PDF_Optimizer.Next.click()
            app.PDF_Optimizer.TNewCheckListBox.click()
            app.PDF_Optimizer.Next.click()
            app.PDF_Optimizer.Install.click()
            app.PDF_Optimizer.Finish.click()

        # Linux install. p.communicate is used to accept the EULA. Popen is opened with home as the cwd.
        # To-do: Pass multiple communicates in a way that: accepts EULA, inputs install directory, declines optimizer
        if platform == "Linux":
            from subprocess import Popen, PIPE
            from . import prep as prep
            prep.create_dir(install_target_loc)
            p = Popen(product_installer, cwd=str(os.path.dirname(install_target_loc)), stdin=PIPE, shell=True)
            # encode string to bytes for p.communicate()
            p.communicate(input='y'.encode('utf-8'))
        self.logger.debug("   Installer complete")