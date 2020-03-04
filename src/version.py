import logging, sys
from distutils.version import StrictVersion

class Version:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Version')
        self.logger.debug('Creating an instance of Version')

    # Get the version to use from the user
    # Returns the verified version
    def get_version_from_user(self, product):
        if product == 'alch' or 'checker' or 'optimizer':
            self.logger.debug("Getting" + product + "version from user")
            v = input("Enter " + product + ' version (expecting "X.X.X"):   ')
            self.logger.debug("Received version: " + str(v))
            ver = self.verify_version_arg_input(product, v)
            if ver:
                return v
            else:
                sys.exit()
        elif product == 'apdfl':
            print("not implemented")
            self.logger.debug("Unsupported product selected: " + product)
            sys.exit()
        elif product == 'flip2pdf':
            print("not implemented")
            self.logger.debug("Unsupported product selected: " + product)
            sys.exit()

    # Verifies the version being used is somewhat appropriate (e.g. follows StrictVersion pattern for alch).
    def verify_version_arg_input(self, product, ver):
        if product == 'alch' or 'checker' or 'optimizer':
            self.logger.debug("Verifying " + product + " CLI arg for version: " + ver)
            try:
                StrictVersion(ver)
            except ValueError:
                self.logger.error("Version input is invalid")
                return False
            self.logger.debug("Received version: " + str(ver))
            return True

