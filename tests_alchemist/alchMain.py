import pytest, logging, os, subprocess, zipfile

sampDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "samples")
outDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")

# To add basic output tests, add the PDF to /samples/base and then add the formats required to base_test.py

# To add a new test category (e.g. for additional parameters)
#   1. Create a new directory in /samples to hold the PDFs
#   2. Create a new def function(), using produce_ocr_output() as an example
#   3. Create a new PARAMETER_test.py file in the /tests_alchemist directory, and specify tests, using ocr_test.py as an example

class AlchemistTest:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.AlchemistTest')
        self.logger.debug('Creating an instance of AlchemistTest')

    def pytest_session_finish(self):
        self.logger.info("Alchemist test run complete")

    def pytest_session_start(self):
        self.logger.info("Alchemist test run initiate")

    def pytest_run_test(self, exe, platform):
        self.logger.debug("Received exe: " + str(exe))
        self.logger.debug("Building output to: " + str(outDir))
        self.logger.debug("Samples found in: " + str(sampDir))
        self.produce_base_output(exe)
        self.produce_ocr_output(exe)

        # Additions from QA
        # self.produce_dutch_output(exe)
        # self.produce_french_output(exe)
        # self.produce_german_output(exe)
        # self.produce_italian_output(exe)
        # self.produce_portuguese_output(exe)
        # self.produce_spanish_output(exe)
        # self.produce_fixes_output(exe)
        # self.produce_fixes2_output(exe)

        self.logger.debug("Verifying output")
        pytest.main(["tests_alchemist", "--html=report.html"])

    # DEMO BASE FILES
    def produce_base_output(self, exe):
        # 1. Specify location of PDFs
        collection = "base"
        # 2. Specify output formats you want
        formats = ["xml", "html", "epub"]
        # 3. Loop through all files found there, use only PDFs
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
        # 4. Processing loop through the formats you want
                for format in formats:
                    self.logger.debug("    Producing " + format)
                    self.verify_output_directory(outDir, collection, filename, format)
                    self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, format), "-outputFormat", format)
        # 5 trim the epub metadata files
                    if format == "epub":
                        self.epub_extract(outDir, collection, filename, format)
            # Alch exe, in file (assembled path, name, and extension), out file (assembled path, name, and
            #   extension), then output format argument

    def produce_fixes_output(self, exe):
        # 1. Specify location of PDFs
        collection = "fixes"
        # 2. Specify output formats you want
        formats = ["xml", "html", "epub"]
        # 3. Loop through all files found there, use only PDFs
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
        # 4. Processing loop through the formats you want
                for format in formats:
                    self.logger.debug("    Producing " + format)
                    self.verify_output_directory(outDir, collection, filename, format)
                    self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, format), "-outputFormat", format)
        # 5 trim the epub metadata files
                    if format == "epub":
                        self.epub_extract(outDir, collection, filename, format)

    def produce_fixes2_output(self, exe):
        # 1. Specify location of PDFs
        collection = "fixes2"
        # 2. Specify output formats you want
        formats = ["xml", "html", "epub"]
        # 3. Loop through all files found there, use only PDFs
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
        # 4. Processing loop through the formats you want
                for format in formats:
                    self.logger.debug("    Producing " + format)
                    self.verify_output_directory(outDir, collection, filename, format)
                    self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, format), "-outputFormat", format, "-borderlessTableDetectionOnPages", "none")
        # 5 trim the epub metadata files
                    if format == "epub":
                        self.epub_extract(outDir, collection, filename, format)

    # DEMO ADDING PARAMETERS
    def produce_ocr_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "ocr"
        # 2. Specify formats you want
        formats = ["xml", "html", "epub"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag"]
        ocrLangs = ["eng"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)


    def produce_dutch_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "dutch"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["nld"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # Alch exe, in file (assembled path, name, and extension), out file (assembled path, name,
                            # and extension), output format argument (two arguments for alch_exe), ocrMode, and ocrLang
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)
    def produce_french_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "french"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["fra"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)

    def produce_german_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "german"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["deu"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)

    def produce_italian_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "italian"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["ita"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)

    def produce_portuguese_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "portuguese"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["por"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)

    def produce_spanish_output(self, exe):
        # 1. Specify the location of PDFs
        collection = "spanish"
        # 2. Specify formats you want
        formats = ["xml"]
        # 3. Create lists of parameter options to loop through
        ocrModes = ["tag", "replace"]
        ocrLangs = ["spa"]
        # 4. Loop through all your parameters and formats
        for file in os.listdir(os.path.join(sampDir, collection)):
            if file.endswith(".pdf"):
                self.logger.info("Producing output files for: " + collection + " " + file)
                filename = os.path.splitext(file)[0]
                for ocrMode in ocrModes:
                    for ocrLang in ocrLangs:
                        for format in formats:
                            # debug info
                            self.logger.info("Producing output files for: " + file)
                            self.logger.debug("    Producing " + ocrMode + " " + ocrLang + " " + format)
                            # The output location is derived from the parameters and the format. Just list them all here
                            outputLocation = [ocrMode, ocrLang, format]
                            self.verify_output_directory(outDir, collection, filename, ocrMode, ocrLang, format)
                            # 4. Call alch_exe and pass it your list of parameters
                            self.alch_exe(str(exe), os.path.join(sampDir, collection, file), os.path.join(outDir, collection, filename, *outputLocation), "-outputFormat", format, "-ocrMode", ocrMode, "-ocrLanguage", ocrLang)
                            # 5. Extract and clean the epub files
                            if format == "epub":
                                self.epub_extract(outDir, collection, filename, *outputLocation)
    def alch_exe(self, *arg):
        subprocess.run([*arg])

    # An epub file is just an archive. We extract the contents and remove the metadata that varies by time, which would
    # otherwise cause false positives
    def epub_extract(self, outDir, sampCategory, filename, *arg):
        self.logger.debug("         Extracting epub file contents")
        with zipfile.ZipFile(os.path.join(outDir, sampCategory, filename, *arg, filename + ".epub"), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(outDir, sampCategory, filename, *arg))
        self.logger.debug("         Removing old epub file")
        os.remove(os.path.join(outDir, sampCategory, filename, *arg, filename + ".epub"))
        self.logger.debug("         Removing package.opf metadata file")
        os.remove(os.path.join(outDir, sampCategory, filename, *arg, "OPS", "package.opf"))

    def verify_output_directory(self, *arg):
        if not os.path.exists(os.path.join(*arg)):
            self.logger.debug("    Creating output directory for this file")
            os.makedirs(os.path.join(*arg))