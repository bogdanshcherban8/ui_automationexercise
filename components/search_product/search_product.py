import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.input import Input
from components.elements.text import Text


class SearchProduct(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.special_offer_image=Image(page, '//*[@id="sale_image"]', "sale_image")
        self.all_products_title=Text(page, '//h2[normalize-space()="All Products"]', "All Products")
        self.search_product_input=Input(page, '//*[@id="search_product"]', "Search Product")
        self.search_button=Button(page, '//*[@id="submit_search"]', "Search button")
        self.search_icon=Icon(page, '//*[@id="submit_search"]/i', "fa fa-search")
        self.searched_products_title=Text(page, '//h2[normalize-space()="Searched Products"]', "Searched Products")
    def check_container(self):
        self.check_url("products")
        self.special_offer_image.to_be_visible()
        self.special_offer_image.to_have_attribute("src", "/static/images/shop/sale.jpg")
        self.all_products_title.to_be_visible()
        self.all_products_title.to_have_text("All Products")
    def check_search_product(self):
        self.search_product_input.to_be_visible()
        self.search_product_input.to_have_attribute("placeholder", "Search Product")
        self.search_product_input.fill("Blue Top")
        self.search_button.to_be_visible()
        self.search_button.to_be_enabled()
        self.search_icon.to_be_visible()
        self.search_icon.to_have_class("fa fa-search")
        self.search_button.click()
        self.searched_products_title.to_be_visible()
        self.searched_products_title.to_have_text("Searched Products")
        self.check_url("products?search=Blue%20Top")
    def check_url(self, text:str):
        self.check_current_url(re.compile(rf'.*/{re.escape(text)}', re.IGNORECASE))