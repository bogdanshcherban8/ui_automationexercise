import allure
from playwright.sync_api import expect

from components.elements.base_element import BaseElement
from tools.logger import get_logger

logger=get_logger("BUTTON")

class Button(BaseElement):
    @property
    def type_of(self)->str:
        return "button"
    def to_be_enabled(self):
        step=f"Checking that {self.type_of} {self.name} is enabled"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            expect(locator).to_be_enabled()

    def to_be_disabled(self):
        step=f"Checking that {self.type_of} {self.name} is disabled"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_disabled()
