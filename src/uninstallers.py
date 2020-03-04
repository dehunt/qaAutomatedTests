import os, logging, time, warnings, shutil, sys
# import pywinauto
# from time import sleep

log = logging.getLogger('qaAutomatedTesting')
warnings.simplefilter('ignore', category=UserWarning) # filters out the 32b / 64b app warning from pywinauto

class AppUninstall:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Uninstall')
        self.logger.debug('Creating an instance of Uninstall')

    # Calls the appropriate uninstall command logic for the product received
    # These uninstall functions will uninstall the product on windows using pywinauto to navigate the GUI
    # And on linux with shutil.rmtree
    def uninstall_product(self, product, platform, default_install_loc, config):
        if product == "alch":
            self.uninstall_alchemist(platform, default_install_loc, config)
        elif product == "checker":
            self.uninstall_checker(platform, default_install_loc, config)
        elif product == "optimizer":
            self.uninstall_optimizer(platform, default_install_loc, config)
        elif product == "apdfl":
            self.uninstall_apdfl(platform, default_install_loc, config)
        elif product == "flip2pdf":
            self.uninstall_flip2pdf(platform, default_install_loc, config)
        else:
            self.logger.critical("No product logic found for " + product)
            sys.exit()

    # def uninstaller_ui_workflow(self, uninstaller, prod_window):
    #     self.logger.debug("Uninstaller UI workflow for " + prod_window)
    #     app = pywinauto.Application(backend="win32").start(str(uninstaller))
    #     window_title = '.*' + prod_window + '.*Uninstall'
    #     app = pywinauto.Application().connect(title_re=window_title)
    #     return app

    def uninstall_alchemist(self, plt, dil, config):
        self.logger.debug("Uninstall product: Alchemist")
        if plt == "Windows":
            import pywinauto
            self.logger.debug("   Uninstall platform: Windows")
            uninstaller = os.path.join(dil, config['u_checker_win'])
            self.logger.debug("   Uninstaller is: " + str(uninstaller))
            # app = self.uninstaller_ui_workflow(uninstaller, "PDF Alchemist")
            app = pywinauto.Application(backend="win32").start(uninstaller)
            time.sleep(2)
            app = pywinauto.Application().connect(title_re=".*PDF Alchemist.*Uninstall", visible_only="true")
            pywinauto.timings.Timings.slow()
            # dlg = app.Uninstall
            app.PDF_Alchemist_Premium_Uninstall.Yes.click()
            app.PDF_Alchemist_Premium_Uninstall.Ok.click()
        if plt == "Linux":
            self.logger.debug("   Uninstall platform: Linux")
            shutil.rmtree(dil)
        self.logger.debug("   Uninstaller complete")

    def uninstall_checker(self, plt, dil, config):
        self.logger.debug("Uninstall product: Checker")
        if plt == "Windows":
            import pywinauto
            self.logger.debug("   Uninstall platform: Windows")
            uninstaller = os.path.join(dil, config['u_checker_win'])
            self.logger.debug("   Uninstaller is: " + str(uninstaller))
            app = pywinauto.Application(backend="win32").start(uninstaller)
            time.sleep(2)
            app = pywinauto.Application().connect(title_re="PDF Checker Uninstall", visible_only="true")
            pywinauto.timings.Timings.slow()
            app.PDF_Checker_Uninstall.Yes.click()
            app.PDF_Checker_Uninstall.Ok.click()
        if plt == "Linux":
            self.logger.debug("   Uninstall platform: Linux")
            shutil.rmtree(dil)
        self.logger.debug("   Uninstaller complete")

    def uninstall_optimizer(self, plt, dil, config):
        self.logger.debug("Uninstall product: Optimizer")
        if plt == "Windows":
            import pywinauto
            self.logger.debug("   Uninstall platform: Windows")
            uninstaller = os.path.join(dil, config['u_optimizer_win'])
            app = pywinauto.Application(backend="win32").start(uninstaller)
            time.sleep(2)
            app = pywinauto.Application().connect(title_re="PDF Optimizer Uninstall", visible_only="true")
            pywinauto.timings.Timings.slow()
            app.PDF_Optimizer_Uninstall.Yes.click()
            app.PDF_Optimizer_Uninstall.Ok.click()
        if plt == "Linux":
            self.logger.debug("   Uninstall platform: Linux")
            shutil.rmtree(dil)
        self.logger.debug("   Uninstaller complete")

    def uninstall_apdfl(self, plt, dil, config):
        self.logger.debug("Uninstall product: APDFL")
        if plt == "Windows":
            self.logger.debug("   Uninstall platform: Windows")
        if plt == "Linux":
            self.logger.debug("   Uninstall platform: Linux")

    def uninstall_flip2pdf(self, plt, dil, config):
        self.logger.debug("Uninstall product: Flip2PDF")
        if plt == "Windows":
            self.logger.debug("   Uninstall platform: Windows")
        if plt == "Linux":
            self.logger.debug("   Uninstall platform: Linux")