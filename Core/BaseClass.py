from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from collections import OrderedDict
import platform
from selenium import webdriver
from pathlib import Path
import sys
import pytest
import os


class BaseClass:
    driver: WebDriver = None

    def __init__(self):
        super(BaseClass).__init__()

    def start_execution(self):
        self.init_driver()
        pytest.main(["-s", "-q", f"{os.getcwd()}/prototype_framework/src/TestCases.py"])

    def stop_execution(self):
        if self.driver:
            self.driver.quit()

    def init_driver(self):
        config = {"Browser": "chrome"}
        driver_location = Path("D:\\Data\\Personal\\PySelFrame\\executables")
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

            BaseClass.driver = driver[driver_type]["interface"](
                executable_path=os.path.join(driver_location, driver[driver_type]["name"]))
            BaseClass.driver.maximize_window()
        except (FileNotFoundError, WebDriverException):
            print(f"{driver[driver_type]['name']} needs to be in drivers folder or PATH")
            sys.exit()
        except Exception as err:
            print(err)
            sys.exit()
