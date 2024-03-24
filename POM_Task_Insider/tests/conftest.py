import pytest
from base.base_test import BaseTest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    bt = BaseTest()
    if result.when == 'call' or (result.when == 'setup' and result.failed):
        case_name = result.nodeid
        path = result.fspath
        if result.failed:
            stack_trace = result.longreprtext + "\n" + result.capstdout
            bt.take_screenshot()
        else:
            stack_trace = result.capstdout
        status = result.outcome
        duration = result.duration
        # DataBaseController.insert_data(status, stack_trace)
