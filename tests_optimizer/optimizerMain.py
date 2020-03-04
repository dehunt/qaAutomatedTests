import pytest, logging, os, subprocess, zipfile

sampDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "samples")
outDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")
profDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "profiles")

# To add basic output tests, add the PDF to /samples/base and then add the formats required to base_test.py

# To add a new test category (e.g. for additional parameters).
#   1. Create a new directory in /samples to hold the PDFs
#   2. Create a new def function(), using produce_base_output() as an example
#   3. Create a new PARAMETER_test.py file in the /tests_checker directory, and specify tests, using base_test.py
#   as an example
# This will accommodate new PDF collections

# To add additional test profiles, add the profile to "profiles", then add the profile name to the profiles list
# This is intended to use additional profiles with existing PDF collections

class OptimizerTest:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.OptimizerTest')
        self.logger.debug('Creating an instance of OptimizerTest')

    def pytest_session_finish(self):
        self.logger.info("Optimizer test run complete")

    def pytest_session_start(self):
        self.logger.info("Optimizer test run initiate")

    def pytest_run_test(self, exe, platform):
        self.logger.debug("Received exe: " + str(exe))
        self.logger.debug("Building output to: " + str(outDir))
        self.logger.debug("Samples found in: " + str(sampDir))
        self.produce_base_output(exe)

        self.logger.debug("Verifying output")
        pytest.main(["tests_optimizer", "-s", "--html=report.html"])

    # DEMO BASE FILES
    # Since the output is a simple text file, it can all be placed into the same output directory.
    # Unlike alchemist, where we wanted to keep xml, html, and epub output split up (or some files replaced others)
    # We'll organize by profile, so that QA can add profiles as desired, while using the same test PDFs.
    def produce_base_output(self, exe):
        # 1. Specify location of PDFs
        collection = "base"
        # 2. Specify the list of test directories. The naming pattern for this baseline is that the main profile matches
        #   the direcctory name, and then the mobile profile version had "mobile_" prepended. So we can use the
        #   directory name to also build profile names.
        # Note that there are some lingering docx files that aren't used by this script. Those were notes from QA that
        #   happened to be in the directory already.
        test_dir = ["Cleanup", "ColorConversion", "Font", "Image", "Objects", "PDFA1B_Conversion", "Transparency", "Userdata"]
        # 3. Loop through all files found there, use only PDFs. Many tests only have one file, but there's no reason
        #   not to do it this way to accommodate adding additional PDFs in the future.
        # We're running this twice, once for the non-mobile profile and once for the mobile profile.
        for test in test_dir:
            self.logger.info("Producing output files for test: " + test)
            self.verify_output_directory(outDir, collection, test)
            for file in os.listdir(os.path.join(sampDir, collection, test)):
                if file.endswith(".pdf"):
                    self.logger.info("Producing output files for: " + collection + " " + test + " " + file)
                    self.optimizer_exe(str(exe), "--input", os.path.join(sampDir, collection, test, file),
                                     "--output", os.path.join(outDir, collection, test, test + '_' + file),
                                     "--profile", os.path.join(sampDir, collection, test, test + '.json'))
                    self.optimizer_exe(str(exe), "--input", os.path.join(sampDir, collection, test, file),
                                       "--output", os.path.join(outDir, collection, test, 'mobile_' + test + '_' + file),
                                       "--profile", os.path.join(sampDir, collection, test, 'mobile_' + test + '.json'))

    # Pass this the entire list of items that will then be assembled for subprocess.run
    def optimizer_exe(self, *arg):
        subprocess.run([*arg], stdout=subprocess.DEVNULL)
        # subprocess.run([*arg])

    def verify_output_directory(self, *arg):
        if not os.path.exists(os.path.join(*arg)):
            self.logger.debug("    Creating output directory for this file")
            os.makedirs(os.path.join(*arg))