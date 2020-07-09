from selenium.common.exceptions import WebDriverException
from collections import OrderedDict
import platform
from selenium import webdriver
import sys
import os

from Core.Logger import Logger
from Core.BaseClass import BaseClass


class Browsers(Logger):
    def open_browser(self):
        driver_type = self.driver_type.lower()
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
                executable_path=os.path.join(self.driver_location, driver[driver_type]["name"]))
            driver = BaseClass.driver
            BaseClass.driver.maximize_window()
            return BaseClass.driver
        except (FileNotFoundError, WebDriverException):
            print(f"{driver[driver_type]['name']} needs to be in drivers folder or PATH")
            sys.exit()
        except Exception as err:
            print(err)
            sys.exit()
