from playwright.sync_api import Page

from components.contact_us.contact_us import ContactUs
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.contact_us=ContactUs(page)