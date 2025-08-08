from components.elements.base_element import BaseElement


class List(BaseElement):
    def select_option(self, value:str):
        locator=self.get_locator()
        locator.select_option(value)
