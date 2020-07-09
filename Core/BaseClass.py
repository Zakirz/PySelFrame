from selenium.webdriver.remote.webdriver import WebDriver
import logging


class BaseClass:
    driver: WebDriver = None
    log: logging = None
