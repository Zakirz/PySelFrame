from Core.BaseClass import BaseClass

import re
import time


class BrowserHelpers(BaseClass):
    locator = None
    locator_type = None
    locator_description = None

    def parse_locator(self, object_locator):
        try:
            pattern = r"^[a-zA-Z0-9_]*#([a-zA-Z_]+)=([\w\[\]()/@\'\":.+=#^$>*\-_])+$"
            if re.match(pattern, object_locator):
                self.locator_description = object_locator.split("#", 1)[0]
                self.locator_type, self.locator = object_locator.split("#", 1)[
                    1].split("=", 1)
            else:
                self.locator_description = object_locator.split("#", 1)[0]
                self.locator_type, self.locator = object_locator.split("#", 1)[
                    1].split("=", 1)
        except re.error as err:
            print(err)

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
            time.sleep(3)
            elements = method(self.locator)
        return elements
