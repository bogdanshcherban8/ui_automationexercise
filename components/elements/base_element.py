from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page:Page, locator:str, name:str):
        self.page=page
        self.locator=locator
        self.name=name

    def get_locator(self)->Locator:
        return self.page.locator(f'xpath={self.locator}')
    def to_be_visible(self):
        locator=self.get_locator()
        expect(locator).to_be_visible()
    def to_have_text(self, text:str):
        locator=self.get_locator()
        expect(locator).to_have_text(text)
    def to_have_attribute(self, name:str, value:str):
        locator=self.get_locator()
        expect(locator).to_have_attribute(name, value)
    def click(self):
        locator=self.get_locator()
        locator.click()
    def to_have_class(self, class_name:str):
        locator=self.get_locator()
        expect(locator).to_have_class(class_name)
    def is_visible(self):
        locator=self.get_locator()
        locator.is_visible()
    def wait_for(self):
        locator=self.get_locator()
        locator.wait_for(state="visible", timeout=2000)
    def to_have_value(self, value:str):
        locator=self.get_locator()
        expect(locator).to_have_value(value)
    def hover(self):
        locator=self.get_locator()
        locator.hover()
