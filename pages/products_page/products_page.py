from playwright.sync_api import Page

from components.brands.brands import Brands
from components.breadcrumb.breadcrumb import Breadcrumb
from components.category.category import Category
from components.current_item.current_item import CurrentItem
from components.items.items import Items
from components.search_product.search_product import SearchProduct
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.search_product=SearchProduct(page)
        self.items=Items(page)
        self.current_item=CurrentItem(page)
        self.category=Category(page)
        self.brands=Brands(page)
        self.breadcrumb=Breadcrumb(page)