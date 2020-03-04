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

class TestAlice(object):
    aliceOut = os.path.join(outDir, 'Alice')
    aliceBase = os.path.join(baseDir, 'Alice')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'xml'), os.path.join(self.aliceBase, 'xml'))
        assert retval == True, "Alice xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'html'), os.path.join(self.aliceBase, 'html'))
        assert retval == True, "Alice html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.aliceOut, 'epub'), os.path.join(self.aliceBase, 'epub'))
        assert retval == True, "Alice epub failed"

class Test080(object):
    formalOut = os.path.join(outDir, '080_Formal_Grammars')
    formalBase = os.path.join(baseDir, '080_Formal_Grammars')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.formalOut, 'xml'), os.path.join(self.formalBase, 'xml'))
        assert retval == True, "080_Formal_Grammars xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.formalOut, 'html'), os.path.join(self.formalBase, 'html'))
        assert retval == True, "080_Formal_Grammars html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.formalOut, 'epub'), os.path.join(self.formalBase, 'epub'))
        assert retval == True, "080_Formal_Grammars epub failed"

class TestBookmarks(object):
    bookmarksOut = os.path.join(outDir, 'AddBookmarks-out')
    bookmarksBase = os.path.join(baseDir, 'AddBookmarks-out')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.bookmarksOut, 'xml'), os.path.join(self.bookmarksBase, 'xml'))
        assert retval == True, "AddBookmarks-out xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.bookmarksOut, 'html'), os.path.join(self.bookmarksBase, 'html'))
        assert retval == True, "AddBookmarks-out html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.bookmarksOut, 'epub'), os.path.join(self.bookmarksBase, 'epub'))
        assert retval == True, "AddBookmarks-out epub failed"

class TestAllstar(object):
    allstarOut = os.path.join(outDir, 'Altarset2')
    allstarBase = os.path.join(baseDir, 'Altarset2')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.allstarOut, 'xml'), os.path.join(self.allstarBase, 'xml'))
        assert retval == True, "Altarset2 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.allstarOut, 'html'), os.path.join(self.allstarBase, 'html'))
        assert retval == True, "Altarset2 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.allstarOut, 'epub'), os.path.join(self.allstarBase, 'epub'))
        assert retval == True, "Altarset2 epub failed"

class TestAssetsBorder(object):
    assetsBorderOut = os.path.join(outDir, 'Assets-border')
    assetsBorderBase = os.path.join(baseDir, 'Assets-border')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.assetsBorderOut, 'xml'), os.path.join(self.assetsBorderBase, 'xml'))
        assert retval == True, "Assets-border xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.assetsBorderOut, 'html'), os.path.join(self.assetsBorderBase, 'html'))
        assert retval == True, "Assets-border html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.assetsBorderOut, 'epub'), os.path.join(self.assetsBorderBase, 'epub'))
        assert retval == True, "Assets-border epub failed"


class TestBalanceSheet(object):
    balanceSheetOut = os.path.join(outDir, 'balance_sheet')
    balanceSheetBase = os.path.join(baseDir, 'balance_sheet')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.balanceSheetOut, 'xml'), os.path.join(self.balanceSheetBase, 'xml'))
        assert retval == True, "balance_sheet xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.balanceSheetOut, 'html'), os.path.join(self.balanceSheetBase, 'html'))
        assert retval == True, "balance_sheet html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.balanceSheetOut, 'epub'), os.path.join(self.balanceSheetBase, 'epub'))
        assert retval == True, "balance_sheet epub failed"


class TestBikeText(object):
    bikeTextOut = os.path.join(outDir, 'BikeText')
    bikeTextBase = os.path.join(baseDir, 'BikeText')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.bikeTextOut, 'xml'), os.path.join(self.bikeTextBase, 'xml'))
        assert retval == True, "BikeText xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.bikeTextOut, 'html'), os.path.join(self.bikeTextBase, 'html'))
        assert retval == True, "BikeText html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.bikeTextOut, 'epub'), os.path.join(self.bikeTextBase, 'epub'))
        assert retval == True, "BikeText epub failed"


class TestBlackwell(object):
    blackwellOut = os.path.join(outDir, 'blackwell')
    blackwellBase = os.path.join(baseDir, 'blackwell')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.blackwellOut, 'xml'), os.path.join(self.blackwellBase, 'xml'))
        assert retval == True, "blackwell xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.blackwellOut, 'html'), os.path.join(self.blackwellBase, 'html'))
        assert retval == True, "blackwell html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.blackwellOut, 'epub'), os.path.join(self.blackwellBase, 'epub'))
        assert retval == True, "blackwell epub failed"


class TestBookgreen(object):
    bookgreenOut = os.path.join(outDir, 'Bookgreen')
    bookgreenBase = os.path.join(baseDir, 'Bookgreen')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.bookgreenOut, 'xml'), os.path.join(self.bookgreenBase, 'xml'))
        assert retval == True, "Bookgreen xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.bookgreenOut, 'html'), os.path.join(self.bookgreenBase, 'html'))
        assert retval == True, "Bookgreen html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.bookgreenOut, 'epub'), os.path.join(self.bookgreenBase, 'epub'))
        assert retval == True, "Bookgreen epub failed"


class TestBookheaderLHJ(object):
    bookheaderLhjOut = os.path.join(outDir, 'BookheaderLHJ')
    bookheaderLhjBase = os.path.join(baseDir, 'BookheaderLHJ')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.bookheaderLhjOut, 'xml'), os.path.join(self.bookheaderLhjBase, 'xml'))
        assert retval == True, "BookheaderLHJ xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.bookheaderLhjOut, 'html'), os.path.join(self.bookheaderLhjBase, 'html'))
        assert retval == True, "BookheaderLHJ html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.bookheaderLhjOut, 'epub'), os.path.join(self.bookheaderLhjBase, 'epub'))
        assert retval == True, "BookheaderLHJ epub failed"


class TestExperiment(object):
    experimentOut = os.path.join(outDir, 'experiment')
    experimentBase = os.path.join(baseDir, 'experiment')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.experimentOut, 'xml'), os.path.join(self.experimentBase, 'xml'))
        assert retval == True, "experiment xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.experimentOut, 'html'), os.path.join(self.experimentBase, 'html'))
        assert retval == True, "experiment html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.experimentOut, 'epub'), os.path.join(self.experimentBase, 'epub'))
        assert retval == True, "experiment epub failed"


class TestLandscape(object):
    landscapeOut = os.path.join(outDir, 'landscape')
    landscapeBase = os.path.join(baseDir, 'landscape')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.landscapeOut, 'xml'), os.path.join(self.landscapeBase, 'xml'))
        assert retval == True, "landscape xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.landscapeOut, 'html'), os.path.join(self.landscapeBase, 'html'))
        assert retval == True, "landscape html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.landscapeOut, 'epub'), os.path.join(self.landscapeBase, 'epub'))
        assert retval == True, "landscape epub failed"


class TestLtn2011(object):
    ltn2011Out = os.path.join(outDir, 'ltn20110921133')
    ltn2011Base = os.path.join(baseDir, 'ltn20110921133')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.ltn2011Out, 'xml'), os.path.join(self.ltn2011Base, 'xml'))
        assert retval == True, "ltn20110921133 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.ltn2011Out, 'html'), os.path.join(self.ltn2011Base, 'html'))
        assert retval == True, "ltn20110921133 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.ltn2011Out, 'epub'), os.path.join(self.ltn2011Base, 'epub'))
        assert retval == True, "ltn20110921133 epub failed"


class TestOffsetRow2(object):
    offsetRow2Out = os.path.join(outDir, 'offset-row2')
    offsetRow2Base = os.path.join(baseDir, 'offset-row2')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2Out, 'xml'), os.path.join(self.offsetRow2Base, 'xml'))
        assert retval == True, "offset-row2 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2Out, 'html'), os.path.join(self.offsetRow2Base, 'html'))
        assert retval == True, "offset-row2 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2Out, 'epub'), os.path.join(self.offsetRow2Base, 'epub'))
        assert retval == True, "offset-row2 epub failed"


class TestOffsetRow2Seven(object):
    offsetRow2SevenOut = os.path.join(outDir, 'offset-row2-7')
    offsetRow2SevenBase = os.path.join(baseDir, 'offset-row2-7')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2SevenOut, 'xml'), os.path.join(self.offsetRow2SevenBase, 'xml'))
        assert retval == True, "offset-row2-7 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2SevenOut, 'html'), os.path.join(self.offsetRow2SevenBase, 'html'))
        assert retval == True, "offset-row2-7 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.offsetRow2SevenOut, 'epub'), os.path.join(self.offsetRow2SevenBase, 'epub'))
        assert retval == True, "offset-row2-7 epub failed"


class TestPlLandscape(object):
    plLandscapeOut = os.path.join(outDir, 'P&L_landscape')
    plLandscapeBase = os.path.join(baseDir, 'P&L_landscape')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.plLandscapeOut, 'xml'), os.path.join(self.plLandscapeBase, 'xml'))
        assert retval == True, "P&L_landscape xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.plLandscapeOut, 'html'), os.path.join(self.plLandscapeBase, 'html'))
        assert retval == True, "P&L_landscape html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.plLandscapeOut, 'epub'), os.path.join(self.plLandscapeBase, 'epub'))
        assert retval == True, "P&L_landscape epub failed"


class TestPlPortraitSaveAsPdf(object):
    plPortraitSaveAsPdfOut = os.path.join(outDir, 'P&L_Portrait_Save_as_PDF')
    plPortraitSaveAsPdfBase = os.path.join(baseDir, 'P&L_Portrait_Save_as_PDF')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.plPortraitSaveAsPdfOut, 'xml'), os.path.join(self.plPortraitSaveAsPdfBase, 'xml'))
        assert retval == True, "P&L_Portrait_Save_as_PDF xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.plPortraitSaveAsPdfOut, 'html'), os.path.join(self.plPortraitSaveAsPdfBase, 'html'))
        assert retval == True, "P&L_Portrait_Save_as_PDF html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.plPortraitSaveAsPdfOut, 'epub'), os.path.join(self.plPortraitSaveAsPdfBase, 'epub'))
        assert retval == True, "P&L_Portrait_Save_as_PDF epub failed"


class TestSample3(object):
    sample3Out = os.path.join(outDir, 'sample3')
    sample3Base = os.path.join(baseDir, 'sample3')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.sample3Out, 'xml'), os.path.join(self.sample3Base, 'xml'))
        assert retval == True, "sample3 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.sample3Out, 'html'), os.path.join(self.sample3Base, 'html'))
        assert retval == True, "sample3 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.sample3Out, 'epub'), os.path.join(self.sample3Base, 'epub'))
        assert retval == True, "sample3 epub failed"


class TestSimple001(object):
    simple001Out = os.path.join(outDir, 'Simple001')
    simple001Base = os.path.join(baseDir, 'Simple001')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.simple001Out, 'xml'), os.path.join(self.simple001Base, 'xml'))
        assert retval == True, "Simple001 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.simple001Out, 'html'), os.path.join(self.simple001Base, 'html'))
        assert retval == True, "Simple001 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.simple001Out, 'epub'), os.path.join(self.simple001Base, 'epub'))
        assert retval == True, "Simple001 epub failed"


class TestSimpleStraddleHeading(object):
    simpleStraddleHeadingOut = os.path.join(outDir, 'Simple-straddle-heading')
    simpleStraddleHeadingBase = os.path.join(baseDir, 'Simple-straddle-heading')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.simpleStraddleHeadingOut, 'xml'), os.path.join(self.simpleStraddleHeadingBase, 'xml'))
        assert retval == True, "Simple-straddle-heading xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.simpleStraddleHeadingOut, 'html'), os.path.join(self.simpleStraddleHeadingBase, 'html'))
        assert retval == True, "Simple-straddle-heading html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.simpleStraddleHeadingOut, 'epub'), os.path.join(self.simpleStraddleHeadingBase, 'epub'))
        assert retval == True, "Simple-straddle-heading epub failed"


class TestTableBorder4(object):
    tableBorder4Out = os.path.join(outDir, 'Table-border4')
    tableBorder4Base = os.path.join(baseDir, 'Table-border4')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.tableBorder4Out, 'xml'), os.path.join(self.tableBorder4Base, 'xml'))
        assert retval == True, "Table-border4 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.tableBorder4Out, 'html'), os.path.join(self.tableBorder4Base, 'html'))
        assert retval == True, "Table-border4 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.tableBorder4Out, 'epub'), os.path.join(self.tableBorder4Base, 'epub'))
        assert retval == True, "Table-border4 epub failed"


class TestTableEmptyCell1(object):
    tableEmptyCell1Out = os.path.join(outDir, 'Table-emptycell-1')
    tableEmptyCell1Base = os.path.join(baseDir, 'Table-emptycell-1')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.tableEmptyCell1Out, 'xml'), os.path.join(self.tableEmptyCell1Base, 'xml'))
        assert retval == True, "Table-emptycell-1 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.tableEmptyCell1Out, 'html'), os.path.join(self.tableEmptyCell1Base, 'html'))
        assert retval == True, "Table-emptycell-1 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.tableEmptyCell1Out, 'epub'), os.path.join(self.tableEmptyCell1Base, 'epub'))
        assert retval == True, "Table-emptycell-1 epub failed"


class TestUs004Clean(object):
    us004CleanOut = os.path.join(outDir, 'us-004-clean')
    us004CleanBase = os.path.join(baseDir, 'us-004-clean')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us004CleanOut, 'xml'), os.path.join(self.us004CleanBase, 'xml'))
        assert retval == True, "us-004-clean xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us004CleanOut, 'html'), os.path.join(self.us004CleanBase, 'html'))
        assert retval == True, "us-004-clean html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us004CleanOut, 'epub'), os.path.join(self.us004CleanBase, 'epub'))
        assert retval == True, "us-004-clean epub failed"


class TestUs005(object):
    us005Out = os.path.join(outDir, 'us-005')
    us005Base = os.path.join(baseDir, 'us-005')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us005Out, 'xml'), os.path.join(self.us005Base, 'xml'))
        assert retval == True, "us-005 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us005Out, 'html'), os.path.join(self.us005Base, 'html'))
        assert retval == True, "us-005 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us005Out, 'epub'), os.path.join(self.us005Base, 'epub'))
        assert retval == True, "us-005 epub failed"


class TestUs006(object):
    us006Out = os.path.join(outDir, 'us-006')
    us006Base = os.path.join(baseDir, 'us-006')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us006Out, 'xml'), os.path.join(self.us006Base, 'xml'))
        assert retval == True, "us-006 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us006Out, 'html'), os.path.join(self.us006Base, 'html'))
        assert retval == True, "us-006 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us006Out, 'epub'), os.path.join(self.us006Base, 'epub'))
        assert retval == True, "us-006 epub failed"


class TestUs010(object):
    us010Out = os.path.join(outDir, 'us-010')
    us010Base = os.path.join(baseDir, 'us-010')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us010Out, 'xml'), os.path.join(self.us010Base, 'xml'))
        assert retval == True, "us-010 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us010Out, 'html'), os.path.join(self.us010Base, 'html'))
        assert retval == True, "us-010 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us010Out, 'epub'), os.path.join(self.us010Base, 'epub'))
        assert retval == True, "us-010 epub failed"


class TestUs012(object):
    us012Out = os.path.join(outDir, 'us-012')
    us012Base = os.path.join(baseDir, 'us-012')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us012Out, 'xml'), os.path.join(self.us012Base, 'xml'))
        assert retval == True, "us-012 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us012Out, 'html'), os.path.join(self.us012Base, 'html'))
        assert retval == True, "us-012 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us012Out, 'epub'), os.path.join(self.us012Base, 'epub'))
        assert retval == True, "us-012 epub failed"


class TestUs014(object):
    us014Out = os.path.join(outDir, 'us-014')
    us014Base = os.path.join(baseDir, 'us-014')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us014Out, 'xml'), os.path.join(self.us014Base, 'xml'))
        assert retval == True, "us-014 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us014Out, 'html'), os.path.join(self.us014Base, 'html'))
        assert retval == True, "us-014 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us014Out, 'epub'), os.path.join(self.us014Base, 'epub'))
        assert retval == True, "us-014 epub failed"


class TestUs027(object):
    us027Out = os.path.join(outDir, 'us-027')
    us027Base = os.path.join(baseDir, 'us-027')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us027Out, 'xml'), os.path.join(self.us027Base, 'xml'))
        assert retval == True, "us-027 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us027Out, 'html'), os.path.join(self.us027Base, 'html'))
        assert retval == True, "us-027 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us027Out, 'epub'), os.path.join(self.us027Base, 'epub'))
        assert retval == True, "us-027 epub failed"


class TestUs031A(object):
    us031aOut = os.path.join(outDir, 'us-031a')
    us031aBase = os.path.join(baseDir, 'us-031a')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us031aOut, 'xml'), os.path.join(self.us031aBase, 'xml'))
        assert retval == True, "us-031a xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us031aOut, 'html'), os.path.join(self.us031aBase, 'html'))
        assert retval == True, "us-031ahtml failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us031aOut, 'epub'), os.path.join(self.us031aBase, 'epub'))
        assert retval == True, "us-031a epub failed"


class TestUs036(object):
    us036Out = os.path.join(outDir, 'us-036')
    us036Base = os.path.join(baseDir, 'us-036')

    def test_xml_output(self):
        retval = util.is_same(os.path.join(self.us036Out, 'xml'), os.path.join(self.us036Base, 'xml'))
        assert retval == True, "us-036 xml failed"

    def test_html_output(self):
        retval = util.is_same(os.path.join(self.us036Out, 'html'), os.path.join(self.us036Base, 'html'))
        assert retval == True, "us-036 html failed"

    def test_epub_output(self):
        retval = util.is_same(os.path.join(self.us036Out, 'epub'), os.path.join(self.us036Base, 'epub'))
        assert retval == True, "us-036 epub failed"
