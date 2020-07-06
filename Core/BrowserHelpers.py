from Core.BaseClass import BaseClass
from Core.Locators import Locator


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
