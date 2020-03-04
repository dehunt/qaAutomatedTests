import logging, platform

# Checker has some metadata output lines that need to be skipped (time, paths, etc).
skip_lines = 7


# for PDF Checker, we just need to fetch the lines after the metadata, and let pytest compare
def get_contents(var):
    logging.debug("Fetching contents of: " + var)
    with open(var) as f:
        lines = f.readlines()[skip_lines:]
        return lines


def get_platform():
    return platform.system()
