import hashlib, filecmp, os, logging, platform

class DirectoryCompare:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.AlchemistTest.DirCompare')
        self.logger.debug('Creating an instance of Alchemist.DirCompare')

# dircmp, but with shallow=False instead of True
class dircmp(filecmp.dircmp):
    def phase3(self):
        fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files, shallow=False)
        self.same_files, self.diff_files, self.funny_files = fcomp

def hash(self, incFile):
    # suf = Path(incFile).suffix
    # print("Suf is:")
    # print(suf)
    # Strip carriage return if found, so win matches lin
    hasher = hashlib.md5()
    # with open(incFile, 'rb') as f:
    #     buf = f.read()
    #     if suf == '.txt':
    #         print("txt file detected")
    #         buf = buf.replace(b'\r\n', b'\n')
    # hasher.update(buf)
    a = hasher.hexdigest()
    print("For inFile:" + incFile)
    print("md5 hash result: " + a)
    return (a)

def is_same(dir1, dir2):
    logging.debug("Comparing directories")
    logging.debug("     Dir1: " + dir1)
    logging.debug("     Dir2: " + dir2)
    compared = dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files
        or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True

def get_platform():
    return platform.system()