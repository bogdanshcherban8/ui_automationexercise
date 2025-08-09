from playwright.sync_api import Page

from components.authentication.signup import Signup
from components.scroll_up.scroll_up import ScrollUp

from components.subscription_copyright.subscription_copyright import SubscriptionCopyright
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.subscription_copyright = SubscriptionCopyright(page)
        self.signup=Signup(page)
        self.scroll_up=ScrollUp(page)




