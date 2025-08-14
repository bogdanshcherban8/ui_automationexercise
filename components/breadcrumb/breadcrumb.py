import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.link import Link
from components.elements.text import Text


class Breadcrumb(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.products_breadcrumb=Link(page, '//section//a[@href="/products"]', "Products")
        self.breadcrumb_path=Text(page, '//section//li[@class="active"]', "Women > Dress")
        self.cart_breadcrumb=Link(page, '//section//a[@href="/"]', "Home")
    @allure.step("Checking breadcrumb")
    def check_breadcrumb_products(self, path_text:str):
        if self.cart_breadcrumb.is_visible():
            self.cart_breadcrumb.to_have_text("Home")
            self.cart_breadcrumb.to_have_attribute("href", "/")
            self.breadcrumb_path.to_be_visible()
            self.breadcrumb_path.to_have_text(path_text)
        else:
            self.products_breadcrumb.is_visible()
            self.products_breadcrumb.to_have_text("Products")
            self.products_breadcrumb.to_have_attribute("href", "/products")
            self.breadcrumb_path.to_be_visible()
            self.breadcrumb_path.to_have_text(path_text)