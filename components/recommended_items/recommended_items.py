import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.text import Text


class RecommendedItems(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.recommended_items_text = Text(page, '//h2[normalize-space()="recommended items"]', "Recommended items")
        self.recommended_left_button = Button(page, '//a[@class="left recommended-item-control"]', "Left button")
        self.recommended_right_button = Button(page, '//a[@class="right recommended-item-control"]', "Right button")
        self.recommended_image = Image(page, '//*[@id="recommended-item-carousel"]/div/div[2]/div[1]/div/div/div/img', "Image")
        self.recommended_title = Text(page, '//*[@id="recommended-item-carousel"]/div/div[2]/div[1]/div/div/div/h2', "Rs.1500")
        self.recommended_description = Text(page,
                                            '//*[@id="recommended-item-carousel"]/div/div[2]/div[1]/div/div/div/p',"Stylish Dress")
        self.recommended_add_to_cart_button = Button(page,
                                                     '//*[@id="recommended-item-carousel"]/div/div[2]/div[1]/div/div/div/a',
                                                     "Add to cart")
        self.recommended_add_to_cart_icon = Icon(page,
                                                 '//*[@id="recommended-item-carousel"]/div/div[2]/div[1]/div/div/div/a/i',
                                                 "fa fa-shopping-cart")

    @allure.step("Checking recommended items block")
    def check_recommended_items(self):
        self.recommended_items_text.to_be_visible()
        self.recommended_items_text.to_have_text("recommended items")
        self.recommended_left_button.to_be_visible()
        self.recommended_left_button.to_have_attribute("href", "#recommended-item-carousel")
        self.recommended_right_button.to_be_visible()
        self.recommended_right_button.to_have_attribute("href", "#recommended-item-carousel")
        self.recommended_image.to_be_visible()
        self.recommended_image.to_have_attribute("src", "get_product_picture/4")
        self.recommended_title.to_be_visible()
        self.recommended_title.to_have_text("Rs. 1500")
        self.recommended_description.to_be_visible()
        self.recommended_description.to_have_text("Stylish Dress")
        self.recommended_add_to_cart_button.to_be_visible()
        self.recommended_add_to_cart_button.to_have_text("Add to cart")
        self.recommended_add_to_cart_icon.to_be_visible()
        self.recommended_add_to_cart_icon.to_have_class("fa fa-shopping-cart")
