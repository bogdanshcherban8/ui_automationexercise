import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.text import Text


class Category(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.category_text = Text(page,
                                  '//h2[normalize-space()="Category"]',
                                  "Category")
        self.women_category_button = Button(page, '//a[@href="#Women"]', "Women")
        self.women_category_icon = Icon(page, '//*[@id="accordian"]/div[1]//i[@class="fa fa-plus"]', "fa fa-plus")
        self.women_dress_button = Button(page, '//*[@id="Women"]/div/ul/li[1]/a', "Dress")
        self.women_tops_button = Button(page, '//*[@id="Women"]/div/ul/li[2]/a', "Tops")
        self.women_saree_button = Button(page, '//*[@id="Women"]/div/ul/li[3]/a', "Saree")
        self.men_category_button = Button(page, '//*[@id="accordian"]/div[2]/div[1]/h4/a', "Men")
        self.men_category_icon = Icon(page, '//div[2]//i[@class="fa fa-plus"]', "fa fa-plus")
        self.men_tshirts_button = Button(page, '//*[@id="Men"]/div/ul/li[1]/a', "Tshirts")
        self.men_jeans_button = Button(page, '//*[@id="Men"]/div/ul/li[2]/a', "Jeans")
        self.kids_category_icon = Icon(page, '//div[3]//i[@class="fa fa-plus"]', "fa fa-plus")
        self.kids_category_button = Button(page, '//*[@id="accordian"]/div[3]/div[1]/h4/a', "Kids")
        self.kids_dress_button = Button(page, '//*[@id="Kids"]/div/ul/li[1]/a', "Dress")
        self.kids_tops_shirts_button = Button(page, '//*[@id="Kids"]/div/ul/li[2]/a', "Tops & Shirts ")
        self.item_products_text=Text(page, '/html/body/section/div/div[2]/div[2]/div/h2', "... - ... Products")
        self.item_check=Text(page, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/p', "Item")
    def check_category_title(self):
        self.category_text.to_be_visible()
        self.category_text.to_have_text("Category")

    def check_category_women(self):
        self.women_category_button.to_be_visible()
        self.women_category_button.to_have_text("Women")
        self.women_category_button.to_have_attribute("href", "#Women")
        self.women_category_icon.to_be_visible()
        self.women_category_icon.to_have_class("fa fa-plus")
        self.women_category_button.click()
        self.women_dress_button.to_be_visible()
        self.women_dress_button.to_have_text("Dress")
        self.women_dress_button.to_have_attribute("href", "/category_products/1")
        self.women_tops_button.to_be_visible()
        self.women_tops_button.to_have_text("Tops")
        self.women_tops_button.to_have_attribute("href", "/category_products/2")
        self.women_saree_button.to_be_visible()
        self.women_saree_button.to_have_text("Saree")
        self.women_saree_button.to_have_attribute("href", "/category_products/7")

    def check_category_men(self):
        self.men_category_button.to_be_visible()
        self.men_category_button.to_have_text("Men")
        self.men_category_button.to_have_attribute("href", "#Men")
        self.men_category_icon.to_be_visible()
        self.men_category_icon.to_have_class("fa fa-plus")
        self.men_category_button.click()
        self.men_tshirts_button.to_be_visible()
        self.men_tshirts_button.to_have_text("Tshirts")
        self.men_tshirts_button.to_have_attribute("href", "/category_products/3")
        self.men_jeans_button.to_be_visible()
        self.men_jeans_button.to_have_text("Jeans")
        self.men_jeans_button.to_have_attribute("href", "/category_products/6")

    def check_category_kids(self):
        self.kids_category_button.to_be_visible()
        self.kids_category_button.to_have_text("Kids")
        self.kids_category_button.to_have_attribute("href", "#Kids")
        self.kids_category_icon.to_be_visible()
        self.kids_category_icon.to_have_class("fa fa-plus")
        self.kids_category_button.click()
        self.kids_dress_button.to_be_visible()
        self.kids_dress_button.to_have_text("Dress")
        self.kids_dress_button.to_have_attribute("href", "/category_products/4")
        self.kids_tops_shirts_button.to_be_visible()
        self.kids_tops_shirts_button.to_have_text("Tops & Shirts ")
        self.kids_tops_shirts_button.to_have_attribute("href", "/category_products/5")



    def check_chosen_category(self, category_button, sub_button, expected_title, expected_item, expected_url):
        category_button.click()
        sub_button.click()
        self.item_products_text.to_be_visible()
        self.item_products_text.to_have_text(expected_title)
        self.item_check.to_be_visible()
        self.item_check.to_have_text(expected_item)
        self.check_url(expected_url)

    def check_url(self, text:str):
        self.check_current_url(re.compile(rf'.*/{text}'))