from Core.BaseClass import BaseClass
from Core.Locators import Locator
import time


class BrowserHelpers(BaseClass, Locator):

    def find_element(self, object_locator):
        self.parse_locator(object_locator)
        if self.locator:
            find = {
                "id": getattr(self.driver, 'find_element_by_id'),
                "xpath": getattr(self.driver, 'find_element_by_xpath'),
                "link_text": getattr(self.driver, 'find_element_by_link_text'),
                "partial_link_text": getattr(self.driver, 'find_element_by_partial_link_text'),
                "name": getattr(self.driver, 'find_element_by_name'),
                "tag": getattr(self.driver, 'find_element_by_tag_name'),
                "class": getattr(self.driver, 'find_element_by_class_name'),
                "css": getattr(self.driver, 'find_element_by_css_selector'),
            }
            method = find[self.locator_type]
            element = method(self.locator)
        return element

    def find_elements(self, object_locator):
        elements = None
        self.parse_locator(object_locator)
        if self.locator:
            find = {
                "id": getattr(self.driver, 'find_elements_by_id'),
                "xpath": getattr(self.driver, 'find_elements_by_xpath'),
                "link_text": getattr(self.driver, 'find_elements_by_link_text'),
                "partial_link_text": getattr(self.driver, 'find_elements_by_partial_link_text'),
                "name": getattr(self.driver, 'find_elements_by_name'),
                "tag": getattr(self.driver, 'find_elements_by_tag_name'),
                "class": getattr(self.driver, 'find_elements_by_class_name'),
                "css": getattr(self.driver, 'find_elements_by_css_selector'),
            }
            method = find[self.locator_type]
            elements = method(self.locator)
        return elements

    def enter_text(self, object_locator, text, delay_typing=False, delay_in_seconds=0.5):
        self.find_element(object_locator).clear()
        if not delay_typing:
            self.find_element(object_locator).send_keys(text)
        else:
            for char in text:
                self.find_element(object_locator).send_keys(char)
                time.sleep(delay_in_seconds)

    def clear_text(self, object_locator):
        self.find_element(object_locator).clear()

    def click_on(self, object_locator, *, using_javascript=False):
        if using_javascript:
            self.driver.execute_script("arguments[0].click();", self.find_element(object_locator))
        else:
            self.find_element(object_locator).click()

    def get_text(self, object_locator):
        return self.find_element(object_locator).text

    def is_element_displayed(self, object_locator):
        time.sleep(5)
        element = self.find_element(object_locator)
        status = element.is_displayed()
        return status

    def is_element_present(self, object_locator):
        element = self.find_element(object_locator)
        return element.is_displayed()

    def navigate_to_url(self, url):
        self.driver.get(url)
        self.log(f"Navigate To {url}")

    def wait_for_page_to_load(self):
        wait_time = 0
        try:
            while self.driver.execute_script('return document.readyState;') != 'complete' and wait_time < 60:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                wait_time += 1
                self.wait_time(1)
        except Exception as err:
            print(f"Exception: {err}.Failed to load page.")

    @staticmethod
    def wait_time(time_in_seconds):
        time.sleep(time_in_seconds)
