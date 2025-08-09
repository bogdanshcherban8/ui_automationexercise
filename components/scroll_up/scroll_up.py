from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.icon import Icon
from components.elements.link import Link


class ScrollUp(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.scroll_link=Link(page, '//*[@id="scrollUp"]', "scrollUp")
        self.scroll_icon=Icon(page, '//*[@id="scrollUp"]/i', "fa fa-angle-up")
    def check_scroll_up(self):
        self.page.evaluate(f'window.scrollBy(0, 500)')
        self.scroll_link.to_be_visible()
        self.scroll_link.to_have_attribute("href", "#top")
        self.scroll_icon.to_be_visible()
        self.scroll_icon.to_have_class("fa fa-angle-up")
        self.scroll_link.click()
