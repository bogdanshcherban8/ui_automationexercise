import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self) -> Locator:
        step = f"Getting locator with {self.locator}"
        with allure.step(step):
            logger.info(step)
            return self.page.locator(f'xpath={self.locator}')

    def to_be_visible(self):
        step = f"Checking that {self.type_of} {self.name} is visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_visible()

    def to_have_text(self, text: str):
        step = f"Checking that {self.type_of} {self.name} has text {text}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_text(text)

    def to_have_attribute(self, name: str, value: str):
        step = f"Checking that {self.type_of} {self.name} has attribute{name} {value}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_attribute(name, value)

    def click(self):
        step = f"Clicking {self.type_of} {self.name}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            locator.click()

    def to_have_class(self, class_name: str):
        step = f"Checking that {self.type_of} {self.name} has class {class_name}"
        with allure.step(f"Checking that {self.type_of} {self.name} has class {class_name}"):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_class(class_name)

    def is_visible(self):
        step = f"Checking that {self.type_of} {self.name} is visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            return locator.is_visible()

    def wait_for(self):
        step = f"Waiting for {self.type_of} {self.name}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            locator.wait_for(state="visible", timeout=2000)

    def to_have_value(self, value: str):
        step = f"Checking that {self.type_of} {self.name} has value {value}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_value(value)

    def hover(self):
        step = f"Hovering {self.type_of} {self.name}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            locator.hover()

    def inner_text(self):
        step = f"Getting text {self.type_of} {self.name}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            return locator.inner_text().strip()

    def to_contain_text(self, text: str):
        step = f"Checking that {self.type_of} {self.name} contain text {text}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_contain_text(text)
