import pytest, logging, os, subprocess

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

class CheckerTest:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.CheckerTest')
        self.logger.debug('Creating an instance of CheckerTest')

    def pytest_session_finish(self):
        self.logger.info("Checker test run complete")

    def pytest_session_start(self):
        self.logger.info("Checker test run initiate")

    def pytest_run_test(self, exe, platform):
        self.logger.debug("Received exe: " + str(exe))
        self.logger.debug("Building output to: " + str(outDir))
        self.logger.debug("Samples found in: " + str(sampDir))
        self.produce_base_output(exe)
        self.produce_password_datalogics_output(exe)
        self.produce_password_mypass_output(exe)

        self.logger.debug("Verifying output")
        pytest.main(["tests_checker", "-s", "--html=report.html"])

    # DEMO BASE FILES
    # Since the output is a simple text file, it can all be placed into the same output directory.
    # Unlike alchemist, where we wanted to keep xml, html, and epub output split up (or some files replaced others)
    # We'll organize by profile, so that QA can add profiles as desired, while using the same test PDFs.
    def produce_base_output(self, exe):
        # 1. Specify location of PDFs
        collection = "base"
        # 2. Specify the profile to use. Leave out .json - we'll add it when we pass the argument to checker_exe.
        # This simplifies also using this list for naming output directories
        profiles = ["everything"]
        # 3. Loop through all files found there, use only PDFs
        for profile in profiles:
            self.logger.info("Producing output files for profile: " + profile)
            self.verify_output_directory(outDir, collection, profile)
            for file in os.listdir(os.path.join(sampDir, collection)):
                if file.endswith(".pdf"):
                    self.logger.info("Producing output file for: " + collection + " " + file)
                    filename = os.path.splitext(file)[0]
                    self.checker_exe(str(exe), "--input", os.path.join(sampDir, collection, file),
                                     "--output", os.path.join(outDir, collection, profile, filename + ".txt"),
                                     "--profile", os.path.join(profDir, profile + ".json"))

    # DEMO PASSWORD-DATALOGICS FILES
    def produce_password_datalogics_output(self, exe):
        # 1. Specify location of PDFs
        collection = "password-Datalogics"
        # 2. Specify the profile to use. Leave out .json - we'll add it when we pass the argument to checker_exe.
        # This simplifies also using this list for naming output directories
        profiles = ["everything"]
        # 3. Loop through all files found there, use only PDFs
        for profile in profiles:
            self.logger.info("Producing output files for profile: " + profile)
            self.verify_output_directory(outDir, collection, profile)
            for file in os.listdir(os.path.join(sampDir, collection)):
                if file.endswith(".pdf"):
                    self.logger.info("Producing output file for: " + collection + " " + file)
                    filename = os.path.splitext(file)[0]
                    self.checker_exe(str(exe), "--input", os.path.join(sampDir, collection, file),
                                     "--output", os.path.join(outDir, collection, profile, filename + ".txt"),
                                     "--profile", os.path.join(profDir, profile + ".json"), "--password", "Datalogics")

    def produce_password_mypass_output(self, exe):
        # 1. Specify location of PDFs
        collection = "password-myPass"
        # 2. Specify the profile to use. Leave out .json - we'll add it when we pass the argument to checker_exe.
        # This simplifies also using this list for naming output directories
        profiles = ["everything"]
        # 3. Loop through all files found there, use only PDFs
        for profile in profiles:
            self.logger.info("Producing output files for profile: " + profile)
            self.verify_output_directory(outDir, collection, profile)
            for file in os.listdir(os.path.join(sampDir, collection)):
                if file.endswith(".pdf"):
                    self.logger.info("Producing output file for: " + collection + " " + file)
                    filename = os.path.splitext(file)[0]
                    self.checker_exe(str(exe), "--input", os.path.join(sampDir, collection, file),
                                     "--output", os.path.join(outDir, collection, profile, filename + ".txt"),
                                     "--profile", os.path.join(profDir, profile + ".json"), "--password", "myPass")

    # Pass this the entire list of items that will then be assembled for subprocess.run
    def checker_exe(self, *arg):
        subprocess.run([*arg])

    def verify_output_directory(self, *arg):
        if not os.path.exists(os.path.join(*arg)):
            self.logger.debug("    Creating output directory for this file")
            os.makedirs(os.path.join(*arg))