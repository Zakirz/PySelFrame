import logging
import pytest
from pathlib import Path
import platform
from collections import OrderedDict
import os
from selenium.common.exceptions import WebDriverException
import sys
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

from Core.BaseClass import BaseClass
from Core.Configs import RunConfig

BASE_DIR = os.path.normpath(os.getcwd() + os.sep)
REPORT_DIR = os.path.join(BASE_DIR, "test_report")
if not os.path.exists(REPORT_DIR):
    os.mkdir(REPORT_DIR)
driver = None
log = None


# @pytest.fixture(scope="session", autouse=True)
# def browser():
#     global driver

#     if RunConfig.driver_type == "chrome":
#         driver = webdriver.Chrome()

#     elif RunConfig.driver_type == "firefox":
#         driver = webdriver.Firefox()

#     elif RunConfig.driver_type == "chrome-headless":
#         chrome_options = CH_Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument("--window-size=1920x1080")
#         driver = webdriver.Chrome(options=chrome_options)

#     elif RunConfig.driver_type == "firefox-headless":
#         firefox_options = FF_Options()
#         firefox_options.headless = True
#         driver = webdriver.Firefox(firefox_options=firefox_options)

#     else:
#         raise NameError("Supported Browsers:  chrome, chrome-headless, firefox, firefox-headless")
#     if driver:
#         driver.maximize_window()
#         BaseClass.driver = driver
#     else:
#         sys.exit()
#     return driver


@pytest.fixture(scope="session", autouse=True)
def browser():
    global driver
    config = {"Browser": "chrome"}
    driver_location = Path(f"{os.getcwd()}\\executables")
    driver_type = config['Browser'].lower()

    driver_extension = None
    platform_name = platform.system()
    if platform_name == "Windows":
        driver_extension = ".exe"
    else:
        driver_extension = ""

    try:
        driver = OrderedDict({
            "chrome": {"name": "chromedriver" + driver_extension, "interface": webdriver.Chrome},
            "firefox": {"name": "geckodriver" + driver_extension, "interface": webdriver.Firefox}
        })
        if driver_type not in driver.keys():
            print(f"{driver_type} is not a valid browser. Hence opening chrome instance")
            driver_type = "chrome"

        driver = driver[driver_type]["interface"](
            executable_path=os.path.join(driver_location, driver[driver_type]["name"]))
        driver.maximize_window()
        BaseClass.driver = driver
        return BaseClass.driver
    except (FileNotFoundError, WebDriverException):
        print(f"{driver[driver_type]['name']} needs to be in drivers folder or PATH")
        sys.exit()
    except Exception as err:
        print(err)
        sys.exit()


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield BaseClass.driver
    BaseClass.driver.quit()
    print("Test Ended !!!")


def pytest_addoption(parser):
    parser.addoption(
        "--log", action="store", default="WARNING", help="set logging level"
    )


@pytest.fixture
def start_log():
    global logger
    logger = logging.getLogger(__name__)
    logger.info("Logger Inititated")
    BaseClass.log = logger
    return BaseClass.logg
