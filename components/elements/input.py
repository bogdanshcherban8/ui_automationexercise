import allure

from components.elements.base_element import BaseElement
from tools.logger import get_logger

logger=get_logger("INPUT")
class Input(BaseElement):
    @property
    def type_of(self)->str:
        return "input"
    def fill(self, text:str):
        step=f"Filling {self.type_of} {self.name} with text {text}"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            locator.fill(text)
    def clear(self):
        step=f"Clearing {self.type_of} {self.name}"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            locator.clear()
    def press(self, text:str):
        step=f"Pressing {self.type_of} {self.name} with text {text}"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            locator.press(text)
