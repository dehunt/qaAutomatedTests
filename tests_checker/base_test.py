import pytest, os
from . import utils as util

plat = util.get_platform()
if plat == "Windows":
    baseline = 'baseline-windows'
if plat == "Linux":
    baseline = 'baseline-linux'

# os.path.dirname(os.path.realpath(__file__)) is the test script directory
outDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output', 'base')
baseDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), baseline, 'base')

# Test function template - just add file name to testfile variable
# def test_(self):
#     testfile = ''+'.txt'
#     assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
#            util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestBaseEverything(object):
    everythingOutDir = os.path.join(outDir, 'everything')
    everythingBaseDir = os.path.join(baseDir, 'everything')

    def test_414_instructions(self):
        testfile = '414-instructions'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_414_instructions_A_1a(self):
        testfile = '414-instructions_A-1a'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_AddAttachments(self):
        testfile = 'AddAttachments'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_AdditionalChecksDamagedFiles(self):
        testfile = 'AdditionalChecksDamagedFiles'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_AddLinks(self):
        testfile = 'AddLinks'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Annotations(self):
        testfile = 'Annotations'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_AnnotsNotForViewingAndPrinting(self):
        testfile = 'AnnotsNotForViewingAndPrinting'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_brokenpdf(self):
        testfile = 'brokenpdf'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_configom(self):
        testfile = 'configom'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_corruptMetadata(self):
        testfile = 'corrupt-metadata'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_CreateAnnotations(self):
        testfile = 'CreateAnnotations'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_DocWithManyImagesAndStreamsAndFonts(self):
        testfile = 'DocWithManyImagesAndStreamsAndFonts'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_dsd_a112(self):
        testfile = 'dsd_a112'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Encrypted(self):
        testfile = 'Encrypted'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_essentVoorschotten(self):
        testfile = 'essent-voorschotten'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_extractFrom(self):
        testfile = 'extractFrom'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_FindImageResolutions(self):
        testfile = 'FindImageResolutions'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_hello_broken_1(self):
        testfile = 'hello-broken_1'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_JavaScriptClock(self):
        testfile = 'JavaScriptClock'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_LocallyBuiltSample(self):
        testfile = 'LocallyBuiltSample'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Matrix2DOperationsJavascriptOperations(self):
        testfile = 'Matrix2DOperationsJavascriptOperations'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_OwnerPassword(self):
        testfile = 'OwnerPassword'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_PDF_2_0_with_page_level_output_intent(self):
        testfile = 'PDF_2.0_with_page_level_output_intent'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_PDFannotationtestfile_noappearances(self):
        testfile = 'PDFannotationtestfile-noappearances'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_PDFannotationtestfile_withappearances(self):
        testfile = 'PDFannotationtestfile-withappearances'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_PDFCHECK_34(self):
        testfile = 'PDFCHECK-34'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_PDFCHECK_34a(self):
        testfile = 'PDFCHECK-34a'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Signed_Gibson_PKCS7_DETACHED_Sha256(self):
        testfile = 'Signed_Gibson_PKCS7_DETACHED_Sha256'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_SimplePDF2_0file(self):
        testfile = 'SimplePDF2.0file'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Test_contains_private_data(self):
        testfile = 'Test_contains_private_data'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_TheFlyv3_EN4Rdr(self):
        testfile = 'TheFlyv3_EN4Rdr'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_TheWarOfTheWorlds(self):
        testfile = 'TheWarOfTheWorlds'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Verdana_Unembedded(self):
        testfile = 'Verdana-Unembedded'+'.txt'
        assert util.get_contents(os.path.join(self.everythingBaseDir, testfile)) == \
               util.get_contents(os.path.join(self.everythingOutDir, testfile)), testfile + " failed"