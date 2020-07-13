import os
import pytest

from Core.Configs import RunConfig


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    os.system('start ' + RunConfig.HTML_REPORT_FILE)
