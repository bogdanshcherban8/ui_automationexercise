from playwright.sync_api import Page

from components.brands.brands import Brands
from components.carousel.carousel import Carousel
from components.category.category import Category
from components.navbar.navbar import Navbar
from components.recommended_items.recommended_items import RecommendedItems
from components.scroll_up.scroll_up import ScrollUp
from components.subscription_copyright.subscription_copyright import SubscriptionCopyright
from pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.subscription_copyright=SubscriptionCopyright(page)
        self.scroll_up=ScrollUp(page)
        self.navbar=Navbar(page)
        self.carousel=Carousel(page)
        self.recommended_items=RecommendedItems(page)
        self.category=Category(page)
        self.brands=Brands(page)

