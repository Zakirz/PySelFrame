# import logging
# import pytest
# import os
# from selenium.common.exceptions import WebDriverException
# import sys
# from py.xml import html
# from selenium import webdriver
# from selenium.webdriver import Remote
# from selenium.webdriver.chrome.options import Options as CH_Options
# from selenium.webdriver.firefox.options import Options as FF_Options

# from Core.BaseClass import BaseClass
# # from Core.Configs import RunConfig

# BASE_DIR = os.path.normpath(os.getcwd() + os.sep)
# REPORT_DIR = os.path.join(BASE_DIR, "test_report")
# if not os.path.exists(REPORT_DIR):
#     os.mkdir(REPORT_DIR)
# driver = None
# logger = None


# @pytest.fixture(scope="session", autouse=True)
# def browser_close():
#     yield BaseClass.driver
#     BaseClass.driver.quit()
#     print("Test Ended !!!")
