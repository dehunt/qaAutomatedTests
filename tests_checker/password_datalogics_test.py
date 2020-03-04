import pytest, os
from . import utils as util

plat = util.get_platform()
if plat == "Windows":
    baseline = 'baseline-windows'
if plat == "Linux":
    baseline = 'baseline-linux'

# os.path.dirname(os.path.realpath(__file__)) is the test script directory
outDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output', 'password-Datalogics')
baseDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), baseline, 'password-Datalogics')

# Test function template - just add file name to testfile variable
# def test_(self):
#     testfile = ''+'.txt'
#     assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
#            util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestBaseEverything(object):
    everythingOutDir = os.path.join(outDir, 'everything')
    everythingBaseDir = os.path.join(baseDir, 'everything')

    def test_AddPassword(self):
        testfile = 'AddPassword'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_AddWatermark(self):
        testfile = 'AddWatermark'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"