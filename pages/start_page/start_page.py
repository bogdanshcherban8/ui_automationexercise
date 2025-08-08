from playwright.sync_api import Page

from components.subscription_copyright.subscription_copyright import SubscriptionCopyright
from pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.subscription_copyright=SubscriptionCopyright(page)

