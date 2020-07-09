from pathlib import Path
import os
import time

TEST_START_TIME = time.strftime("%Y_%m_%d_%H_%M_%S")


class RunConfig:
    BASE_DIR = os.path.normpath(os.getcwd() + os.sep)
    REPORT_DIR = os.path.join(BASE_DIR, "Reports")
    if not os.path.exists(REPORT_DIR):
        os.mkdir(REPORT_DIR)

    CURRENT_REPORT_DIR = os.path.join(REPORT_DIR, TEST_START_TIME)
    if not os.path.exists(CURRENT_REPORT_DIR):
        os.mkdir(CURRENT_REPORT_DIR)
        os.mkdir(os.path.join(CURRENT_REPORT_DIR, "image"))

    HTML_REPORT_FILE = os.path.join(REPORT_DIR, TEST_START_TIME, "Result.html")

    XML_REPORT_FILE = os.path.join(REPORT_DIR, TEST_START_TIME, "junit.xml")

    LOG_FILE = os.path.join(REPORT_DIR, TEST_START_TIME, "Logs.txt")

    BROWSER_TYPE = "chrome"

    DRIVERS_PATH = Path(f"{os.getcwd()}\\executables")

    BASE_URL = "https://www.remoteworks.in"

    MAX_FAIL = "2"

    LOG_ID = 0
