from playwright.sync_api import expect

from components.elements.base_element import BaseElement


class Button(BaseElement):
    def to_be_enabled(self):
        locator=self.get_locator()
        expect(locator).to_be_enabled()

    def to_be_disabled(self):
        locator = self.get_locator()
        expect(locator).to_be_disabled()
