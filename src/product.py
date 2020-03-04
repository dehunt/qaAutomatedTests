import logging, sys

class Product:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Product')
        self.logger.debug('Creating an instance of Product')

    # Fetches product from user
    def get_user_product_input(self):
        uin = '0'
        self.logger.debug('Getting product choice from user')
        while uin == '0':
            print("Enter number for corresponding product")
            print("    1: PDF Alchemist")
            print("    2: PDF Checker")
            print("    3: PDF Optimizer")
            print("    9: Cancel")
            uin = input("--> ")
        self.logger.debug('Input received is: ' + str(uin))
        if uin == '9':
            print("Exiting")
            sys.exit()
        if (uin != '1') and (uin != '2') and (uin != '3') and (uin != 9):
            self.logger.debug("Invalid input: " + uin)
            self.logger.info("Invalid input. Exiting.")
            sys.exit()
        else:
            retval = self.get_product_script_name(uin)
            return retval

    # Switcher that selects product
    def get_product_script_name(self, inc):
        switch = {
            1: "alch",
            2: "checker",
            3: "optimizer"
            # 4: "apdfl",
            # 5: "flip2pdf"
        }
        s = switch.get(int(inc), "Invalid option selected")
        self.logger.debug("Product switcher returning " + str(s))
        return s

    # Verifies product argument input
    def verify_product_arg_input(self, var):
        self.logger.debug("Verifying CLI argument for product: " + var)
        product_list = ['alch', 'checker', 'optimizer', 'apdfl', 'flip2pdf']
        if any(var in s for s in product_list):
            self.logger.debug("Returning TRUE")
            return True
        else:
            self.logger.error("Product input is invalid")
            return False

    # Gets the exe name for product
    def get_exe_name(self, prod, plat, config):
        self.logger.debug("Getting executable name for: " + str(prod) + " " + str(plat))
        if plat == "Windows":
            return config["e_"+prod+"_win"]
        if plat == "Linux":
            return config["e_"+prod+"_lin"]