import pytest
from pathlib import Path
import platform
from collections import OrderedDict
import os
from selenium.common.exceptions import WebDriverException
import sys
from py.xml import html
from selenium import webdriver

from Core.BaseClass import BaseClass

BASE_DIR = os.path.normpath(os.getcwd() + os.sep)
REPORT_DIR = os.path.join(BASE_DIR, "test_report")
if not os.path.exists(REPORT_DIR):
    os.mkdir(REPORT_DIR)
driver = None


@pytest.fixture(scope="session", autouse=True)
def init_driver():
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
            print(f"{driver_type} is not a valid browser type. Hence opening chrome instance")
            driver_type = "chrome"

        driver = driver[driver_type]["interface"](
            executable_path=os.path.join(driver_location, driver[driver_type]["name"]))
        driver.maximize_window()
        BaseClass.driver = driver
        return driver
    except (FileNotFoundError, WebDriverException):
        print(f"{driver[driver_type]['name']} needs to be in drivers folder or PATH")
        sys.exit()
    except Exception as err:
        print(err)
        sys.exit()


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


# @pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    global driver
    file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('Run Error')
    image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
    driver.save_screenshot(image_dir)


def new_report_time():
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-2]
    except IndexError:
        return None
