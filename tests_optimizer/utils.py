import logging, platform, string, random
import diff_pdf_visually, PyPDF2


# Accepts two pdfs to compare using diff-pdf-visually module.
# Returns True if visually the same, False otherwise.
# When setting verbosity, can range from 0 to 3
#   0 = quiet
#   1 = default (result and why, sanity warnings, temp dir, rough process
#   2 (significance for each page)
#   3 = max (print PDFToCairo and ImageMagick commands used)
# When setting threshold, default is 100. Lower means ignore more.
# num_threads: number of parallel threads (default 2)
# dpi: default resolution to render pages (default 50)
def compare_pdfs(pdf_a, pdf_b):
    return diff_pdf_visually.pdfdiff(pdf_a, pdf_b, verbosity=0)


# title_raw will return a ByteStringObject
# title will return a Text StringObject or None (if title not specified)
def get_pdf_title(pdf):
    retval = get_pdf_info(pdf)
    return retval.title


# author_raw will return a ByteStringObject
# author will return a Text StringObject or None (if author not specified)
def get_pdf_author(pdf):
    retval = get_pdf_info(pdf)
    return retval.author

# Additional DocumentInfo options are subject, creator, producer, and their _raw versions
def get_pdf_info(in_pdf):
    with open(in_pdf, 'rb') as pdf:
        frd = PyPDF2.PdfFileReader(pdf)
        return frd.getDocumentInfo()


# Fetching attachments as implemented for this PyPDF2 commit https://github.com/mstamy2/PyPDF2/pull/440/files
# Receives the PDF path, returns a dictionary of the attachments.
# If attachments aren't found, the KeyError is caught and the error message returned.
# We generate a random string of letters and numbers to ensure that the pytest case fails if there are no attachments.
# When using get_attachments() and assert, just directly compare the returned dictionary lists using ==
def get_attachments(test_pdf):
    handler = open(test_pdf, 'rb')
    reader = PyPDF2.PdfFileReader(handler)
    catalog = reader.trailer["/Root"]
    # From the catalog get the embedded file names
    try:
        fileNames = catalog['/Names']['/EmbeddedFiles']['/Names']
        attachments = {}
        # Loop through attachments
        for f in fileNames:
            if isinstance(f, str):
                name = f
                dataIndex = fileNames.index(f) + 1
                fDict = fileNames[dataIndex].getObject()
                fData = fDict['/EF']['/F'].getData()
                attachments[name] = fData
        return attachments
    except KeyError:
        return "No attachments " + test_pdf + "-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def get_platform():
    return platform.system()
