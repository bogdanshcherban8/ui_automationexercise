import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.text import Text


class Brands(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.brands_category_text = Text(page, '//h2[normalize-space()="Brands"]', "Brands")
        self.brands_polo_button = Button(page, '//a[@href="/brand_products/Polo"]', "Polo")
        self.brands_hm_button = Button(page, '//a[@href="/brand_products/H&M"]', "H&M")
        self.brands_madame_button = Button(page, '//a[@href="/brand_products/Madame"]', "Madame")
        self.brands_mast_button = Button(page, '//a[@href="/brand_products/Mast & Harbour"]', "Mast & Harbour")
        self.brands_baby_button = Button(page, '//a[@href="/brand_products/Babyhug"]', "Babyhug")
        self.brands_allen_button = Button(page,
                                          '//a[@href="/brand_products/Allen Solly Junior"]', "Allen Solly Junior")
        self.brands_kookie_button = Button(page,
                                           '//a[@href="/brand_products/Kookie Kids"]', "Kookie Kids")
        self.brands_biba_button = Button(page,
                                         '//a[@href="/brand_products/Biba"]', "Biba")
        self.brands_title = Text(page, '//h2[@class="title text-center"]', "Brand - ... products")
        self.brands_item = Text(page, '//div[2]/div/div[2]//div[@class="productinfo text-center"]/p', "Item")
    @allure.step("Checking brands title")
    def check_brands_title(self):
        self.brands_category_text.to_be_visible()
        self.brands_category_text.to_have_text("Brands")
    @allure.step("Checking brands categories")
    def check_brands(self):
        self.brands_polo_button.to_be_visible()
        self.brands_polo_button.to_have_text("(6)Polo")
        self.brands_polo_button.to_have_attribute("href", "/brand_products/Polo")
        self.brands_hm_button.to_be_visible()
        self.brands_hm_button.to_have_text("(5)H&M")
        self.brands_hm_button.to_have_attribute("href", "/brand_products/H&M")
        self.brands_madame_button.to_be_visible()
        self.brands_madame_button.to_have_text("(5)Madame")
        self.brands_madame_button.to_have_attribute("href", "/brand_products/Madame")
        self.brands_mast_button.to_be_visible()
        self.brands_mast_button.to_have_text("(3)Mast & Harbour")
        self.brands_mast_button.to_have_attribute("href", "/brand_products/Mast & Harbour")
        self.brands_baby_button.to_be_visible()
        self.brands_baby_button.to_have_text("(4)Babyhug")
        self.brands_baby_button.to_have_attribute("href", "/brand_products/Babyhug")
        self.brands_allen_button.to_be_visible()
        self.brands_allen_button.to_have_text("(3)Allen Solly Junior")
        self.brands_allen_button.to_have_attribute("href", "/brand_products/Allen Solly Junior")
        self.brands_kookie_button.to_be_visible()
        self.brands_kookie_button.to_have_text("(3)Kookie Kids")
        self.brands_kookie_button.to_have_attribute("href", "/brand_products/Kookie Kids")
        self.brands_biba_button.to_be_visible()
        self.brands_biba_button.to_have_text("(5)Biba")
        self.brands_biba_button.to_have_attribute("href", "/brand_products/Biba")
    @allure.step("Checking one brand page")
    def check_chosen_brand(self, brand_button, expected_title, expected_item, expected_url):
        brand_button.click()
        self.brands_title.to_be_visible()
        self.brands_title.to_have_text(expected_title)
        self.brands_item.to_be_visible()
        self.brands_item.to_have_text(expected_item)
        self.check_url(expected_url)

    def check_url(self, text: str):
        self.check_current_url(re.compile(rf'.*/{re.escape(text)}'))
