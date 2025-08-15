from playwright.sync_api import Page

from components.authentication.login import Login
from components.breadcrumb.breadcrumb import Breadcrumb
from components.items.items import Items
from components.navbar.navbar import Navbar
from components.scroll_up.scroll_up import ScrollUp
from components.subscription_copyright.subscription_copyright import SubscriptionCopyright
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.subscription_copyright = SubscriptionCopyright(page)
        self.login=Login(page)
        self.items=Items(page)
        self.scroll_up=ScrollUp(page)
        self.navbar=Navbar(page)
        self.breadcrumb=Breadcrumb(page)