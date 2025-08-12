

from components.elements.base_element import BaseElement


class Input(BaseElement):
    def fill(self, text:str):
        locator=self.get_locator()
        locator.fill(text)
    def clear(self):
        locator=self.get_locator()
        locator.clear()
    def press(self, text:str):
        locator=self.get_locator()
        locator.press(text)
