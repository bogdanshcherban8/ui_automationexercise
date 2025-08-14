import allure

from components.elements.base_element import BaseElement
from tools.logger import get_logger

logger=get_logger("LIST")
class List(BaseElement):
    @property
    def type_of(self):
        return "list"
    def select_option(self, value:str):
        step=f"Selecting option {self.type_of} {self.name} with value {value}"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            locator.select_option(value)
