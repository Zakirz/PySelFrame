import os
import sys
import platform
from collections import OrderedDict
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from Core.Logger import Logger


class BaseClass(Logger):
    driver: WebDriver = None

    def start_execution(self):
        self.init_logger()
        self.open_browser()

    def stop_execution(self):
        if self.driver:
            self.driver.quit()

    def open_browser(self):
        driver_type = self.BROWSER_TYPE.lower()
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
                executable_path=os.path.join(self.DRIVERS_PATH, driver[driver_type]["name"]))
            BaseClass.driver = driver
            BaseClass.driver.maximize_window()
            return BaseClass.driver
        except (FileNotFoundError, WebDriverException):
            print(f"{driver[driver_type]['name']} needs to be in drivers folder or PATH")
            sys.exit()
        except Exception as err:
            print(err)
            sys.exit()
