import platform, os, errno, logging, ctypes
# from distutils.version import StrictVersion
# from pathlib import Path, PureWindowsPath

log = logging.getLogger('qaAutomatedTesting')

class Prep:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Prep')
        self.logger.debug('Creating an instance of Prep')

    # Fetches os platform
    def get_platform(self):
        var = platform.system()
        self.logger.debug('Getting platform: %s', var)
        return var

    # Checks if valid platform for product
    def verify_platform(self):
        var = self.get_platform()
        self.logger.debug('Verifying platform')
        if var == "Windows" or var == "Linux":
            self.logger.debug("Platform is: " + str(var))
            return var
        else:
            self.logger.error("Unsupported OS. Supported systems are: Windows, Linux.")
            exit()

# Get current working directory
def get_directory():
    return os.getcwd()

# Verify directory, creates if not found
def create_dir(var):
    if not os.path.isdir(var):
        try:
            os.mkdir(var)
        except FileExistsError:
            pass
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                print("Creation of output directory failed")
                raise
    return var

# Checks if script ran as windows admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False