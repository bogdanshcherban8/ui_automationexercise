from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.link import Link
from components.elements.text import Text


class Items(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.item_image = Image(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/img',
                                "Item image")
        self.price_title=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/h2', "Rs. 500")
        self.item_title=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/p', "Blue Top")
        self.view_link=Link(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a', "View Product")
        self.add_to_cart=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a', "Add to cart")
        self.shopping_cart=Icon(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a/i', "Shopping cart")
        self.overlay_price=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/h2', "Rs. 500")
        self.overlay_title=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/p', "Blue Top")
        self.overlay_add_to_cart=Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a', "Add to cart")
        self.overlay_shopping_cart=Icon(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a/i', "Shopping cart")
        self.icon_box=Icon(page, '//*[@id="cartModal"]/div/div/div[1]/div/i', "")
        self.added_title=Text(page, '//*[@id="cartModal"]/div/div/div[1]/h4', "Added!")
        self.your_product_text=Text(page, '//*[@id="cartModal"]/div/div/div[2]/p[1]', "Your product has been added to cart.")
        self.continue_button=Button(page, '//*[@id="cartModal"]/div/div/div[3]/button', "Continue Shopping")
        self.view_cart_link=Link(page, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a', "View Cart")
        self.item_title_box=Text(page, '//*[@id="cart_info_table"]/thead/tr/td[1]', "Item")
    def check_item(self):
        self.item_image.to_be_visible()
        self.item_image.to_have_attribute("src", "/get_product_picture/1")
        self.price_title.to_be_visible()
        self.price_title.to_have_text("Rs. 500")
        self.item_title.to_be_visible()
        self.item_title.to_have_text("Blue Top")
        self.view_link.to_be_visible()
        self.view_link.to_have_attribute("href", "/product_details/1")
        self.view_link.to_have_text("View Product")
        self.add_to_cart.to_be_visible()
        self.add_to_cart.to_have_text("Add to cart")
        self.shopping_cart.to_be_visible()
        self.shopping_cart.to_have_class("fa fa-shopping-cart")
        self.item_image.hover()
        self.overlay_price.to_be_visible()
        self.overlay_price.to_have_text("Rs. 500")
        self.overlay_title.to_be_visible()
        self.overlay_title.to_have_text("Blue Top")
        self.overlay_add_to_cart.to_be_visible()
        self.overlay_add_to_cart.to_have_text("Add to cart")
        self.overlay_shopping_cart.to_be_visible()
        self.overlay_shopping_cart.to_have_class("fa fa-shopping-cart")
        self.overlay_add_to_cart.click()

    def added_item(self):
        self.icon_box.to_be_visible()
        self.icon_box.to_have_text("")
        self.icon_box.to_have_class("material-icons")
        self.added_title.to_be_visible()
        self.added_title.to_have_text("Added!")
        self.your_product_text.to_be_visible()
        self.your_product_text.to_have_text("Your product has been added to cart.")
        self.continue_button.to_be_visible()
        self.continue_button.to_have_text("Continue Shopping")
        self.continue_button.to_be_enabled()
        self.view_cart_link.to_be_visible()
        self.view_cart_link.to_have_text("View Cart")
        self.view_cart_link.to_have_attribute("href", "/view_cart")
        self.view_cart_link.click()
    def cart_item(self):
        self.item_title_box.to_be_visible()
        self.item_title_box.to_have_text("Item")