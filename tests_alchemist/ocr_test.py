import pytest, os
from . import utils as util

plat = util.get_platform()
if plat == "Windows":
    baseline = 'baseline-windows'
if plat == "Linux":
    baseline = 'baseline-linux'

outDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output', 'ocr')
baseDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), baseline, 'ocr')

class TestAlice(object):
    aliceOut = os.path.join(outDir, 'Alice')
    aliceBase = os.path.join(baseDir, 'Alice')

    def test_tag_eng_xml_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'tag', 'eng', 'xml'), os.path.join(self.aliceBase, 'tag', 'eng', 'xml'))
        assert retval == True, "Alice xml failed"

    def test_tag_eng_html_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'tag', 'eng', 'html'), os.path.join(self.aliceBase, 'tag', 'eng', 'html'))
        assert retval == True, "Alice html failed"

    def test_tag_eng_epub_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'tag', 'eng', 'epub'), os.path.join(self.aliceBase, 'tag', 'eng', 'epub'))
        assert retval == True, "Alice epub failed"