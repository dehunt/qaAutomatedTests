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

# For our attachment tests we're just going to check the names of the attachments, but we can extract them as well by
#   adding this code when handling the dictionary:
# for fName, fData in dictionary.items():
#     with open(fName, 'wb') as outfile:
#         outfile.write(fData)

# For PDF comparison
#     def test_NAME(self):
#         testfile = 'TESTFILE'
#         assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

# For attachment comparison
# def test_NAME(self):
#     testfile = 'TESTFILE'
#     assert util.get_attachments(os.path.join(self.everythingOutDir, testfile)) == util.get_attachments(
#         os.path.join(self.everythingBaseDir, testfile)), testfile + " failed"

# For metadata comparison (title / author / etc)
# def test_NAME(self):
#     testfile = 'TESTFILE'
#     assert util.get_pdf_title(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_title(
#         os.path.join(self.everythingOutDir, testfile)), testfile + " title compare failed"
# def test_NAME(self):
#     testfile = 'TESTFILE'
#     assert util.get_pdf_author(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_author(
#         os.path.join(self.everythingOutDir, testfile)), testfile + " author compare failed"


# NOTE: These tests take ~25 min each because of the number of pages in the test PDFs.
# class TestCleanup(object):
#     everythingOutDir = os.path.join(outDir, 'Cleanup')
#     everythingBaseDir = os.path.join(baseDir, 'Cleanup')
#
#     def test_Multipage_10000_SaskTelBilling(self):
#         testfile = 'Cleanup_Multipage_10000_SaskTelBilling.pdf'
#         assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"
#
#     def test_mobile_Multipage_10000_SaskTelBilling(self):
#         testfile = 'mobile_Cleanup_Multipage_10000_SaskTelBilling.pdf'
#         assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestColorConversion(object):
    everythingOutDir = os.path.join(outDir, 'ColorConversion')
    everythingBaseDir = os.path.join(baseDir, 'ColorConversion')

    def test_ColorConversion_ColorConversion(self):
        testfile = 'ColorConversion_ColorConversion.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_ColorConversion_ColorConversion(self):
        testfile = 'mobile_ColorConversion_ColorConversion.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestFont(object):
    everythingOutDir = os.path.join(outDir, 'Font')
    everythingBaseDir = os.path.join(baseDir, 'Font')

    def test_Font_configom(self):
        testfile = 'Font_configom.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Font_configom(self):
        testfile = 'mobile_Font_configom.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Font_parabolic(self):
        testfile = 'Font_parabolic.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Font_parabolic(self):
        testfile = 'mobile_Font_parabolic.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestImage(object):
    everythingOutDir = os.path.join(outDir, 'Image')
    everythingBaseDir = os.path.join(baseDir, 'Image')

    def test_Image_Final_Fantasy_Adventure_Guide(self):
        testfile = 'Image_Final-Fantasy-Adventure-Guide.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Image_Final_Fantasy_Adventure_Guide(self):
        testfile = 'mobile_Image_Final-Fantasy-Adventure-Guide.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Image_ImageResampling(self):
        testfile = 'Image_ImageResampling.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Image_ImageResampling(self):
        testfile = 'mobile_Image_ImageResampling.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestObjects(object):
    everythingOutDir = os.path.join(outDir, 'Objects')
    everythingBaseDir = os.path.join(baseDir, 'Objects')

    def test_Objects_physics_textbook(self):
        testfile = 'Objects_physics_textbook.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Objects_physics_textbook(self):
        testfile = 'mobile_Objects_physics_textbook.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

# NOTE
# This will currently VISUALLY compare the files, which can identify if they changed but won't catch any
# pdfa1b compliance issues that ARE NOT visually identifiable.
class TestPDFA1BConversion(object):
    everythingOutDir = os.path.join(outDir, 'PDFA1B_Conversion')
    everythingBaseDir = os.path.join(baseDir, 'PDFA1B_Conversion')

    def test_PDFA1B_Conversion_PDFA(self):
        testfile = 'PDFA1B_Conversion_PDFA.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_PDFA1B_Conversion_PDFA(self):
        testfile = 'mobile_PDFA1B_Conversion_PDFA.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestTransparency(object):
    everythingOutDir = os.path.join(outDir, 'Transparency')
    everythingBaseDir = os.path.join(baseDir, 'Transparency')

    def test_Transparency_CreateTransparency(self):
        testfile = 'Transparency_CreateTransparency.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Transparency_CreateTransparency(self):
        testfile = 'mobile_Transparency_CreateTransparency.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

class TestUserdata(object):
    everythingOutDir = os.path.join(outDir, 'Userdata')
    everythingBaseDir = os.path.join(baseDir, 'Userdata')

    def test_Userdata_Attachments(self):
        testfile = 'Userdata_Attachments.pdf'
        assert util.get_attachments(os.path.join(self.everythingOutDir, testfile)) == util.get_attachments(os.path.join(self.everythingBaseDir, testfile)), testfile + " failed"

    def test_mobile_Userdata_Attachments(self):
        testfile = 'mobile_Userdata_Attachments.pdf'
        assert util.get_attachments(os.path.join(self.everythingOutDir, testfile)) == util.get_attachments(os.path.join(self.everythingBaseDir, testfile)), testfile + " failed"

    def test_Userdata_AddLinks(self):
        testfile = 'Userdata_AddLinks.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_mobile_Userdata_AddLinks(self):
        testfile = 'mobile_Userdata_AddLinks.pdf'
        assert util.compare_pdfs(os.path.join(self.everythingBaseDir, testfile), os.path.join(self.everythingOutDir, testfile)), testfile + " failed"

    def test_Userdata_AddDocumentInformation_meta_title(self):
        testfile = 'Userdata_AddDocumentInformation-meta.pdf'
        assert util.get_pdf_title(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_title(os.path.join(self.everythingOutDir, testfile)), testfile + " title compare failed"

    def test_mobile_Userdata_AddDocumentInformation_meta_title(self):
        testfile = 'mobile_Userdata_AddDocumentInformation-meta.pdf'
        assert util.get_pdf_title(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_title(os.path.join(self.everythingOutDir, testfile)), testfile + " title compare failed"

    def test_Userdata_AddDocumentInformation_meta_author(self):
        testfile = 'Userdata_AddDocumentInformation-meta.pdf'
        assert util.get_pdf_author(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_author(os.path.join(self.everythingOutDir, testfile)), testfile + " author compare failed"

    def test_mobile_Userdata_AddDocumentInformation_meta_author(self):
        testfile = 'mobile_Userdata_AddDocumentInformation-meta.pdf'
        assert util.get_pdf_author(os.path.join(self.everythingBaseDir, testfile)) == util.get_pdf_author(os.path.join(self.everythingOutDir, testfile)), testfile + " author compare failed"