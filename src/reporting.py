from datetime import datetime
import logging

class Reporting:
    def __init__(self):
        self.logger = logging.getLogger('qaAutomatedTesting.Report')
        self.logger.debug('Creating an instance of Report')

    def report(self, message):
        self.logger.info(message)

# generates name for logfile
def get_report_filename():
    return 'qaAutoTestReport_' + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.log'

def get_debug_filename():
    return 'qaAutoTestDebugLog_' + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.log'
