from playwright.sync_api import expect

from components.elements.base_element import BaseElement


class Input(BaseElement):
    def fill(self, text:str):
        locator=self.get_locator()
        locator.fill(text)
    def clear(self):
        locator=self.get_locator()
        locator.clear()
