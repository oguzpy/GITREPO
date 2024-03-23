# from base.base_functions import BaseFunctions
# from base.base_test import BaseTest
#
#
# class CaseReporter(BaseTest):
#
#     def __init__(self, item, outcome):
#         self.item = item
#         self.outcome = outcome.get_result()
#         self.driver = BaseTest
#
#     def case_reporter(self):
#         if self.outcome.when == 'call' or (self.outcome.when == 'setup' and self.outcome.failed):
#             case_name = self.outcome.nodeid
#             path = self.outcome.fspath
#             if self.outcome.failed:
#                 stack_trace = self.outcome.longreprtext + "\n" + self.outcome.capstdout
#                 self.driver.save_screenshot("teststst")
#             else:
#                 stack_trace = self.outcome.capstdout
#             status = self.outcome.outcome
#             duration = self.outcome.duration
#             # DataBaseController.insert_data(status, stack_trace)
