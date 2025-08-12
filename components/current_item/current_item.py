from faker import Faker
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.input import Input
from components.elements.link import Link
from components.elements.text import Text


class CurrentItem(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.fake = Faker()
        self.image_current_item = Image(page, '//img[@src="/get_product_picture/1"]', "Current item image")
        self.new_image = Image(page, '//img[@src="/static/images/product-details/new.jpg"]', "newarrival")
        self.item_title = Text(page, '//h2[normalize-space()="Blue Top"]', "Blue Top")
        self.item_path = Text(page, '//p[normalize-space()="Category: Women > Tops"]', "Category: Women > Tops")
        self.stars_image = Image(page, '//img[@src="/static/images/product-details/rating.png"]', "Stars")
        self.price = Text(page, '//span[normalize-space()="Rs. 500"]', "Rs. 500")
        self.quantity = Text(page, '//label[normalize-space()="Quantity:"]', "Quantity:")
        self.quantity_input = Input(page, '//*[@id="quantity"]', "Quantity input")
        self.add_to_cart_button = Button(page, '//button[normalize-space()="Add to cart"]', "Add to cart")
        self.add_to_cart_icon = Icon(page, '//section//i[@class="fa fa-shopping-cart"]', "fa fa-shopping-cart")
        self.availability_text = Text(page, '//p[normalize-space()="Availability: In Stock"]', "Availability: In Stock")
        self.condition_text = Text(page, '//p[normalize-space()="Condition: New"]', "Condition: New")
        self.brand_text = Text(page, '//p[normalize-space()="Brand: Polo"]', "Brand: Polo")
        self.write_review_link = Link(page, '//a[@href="#reviews"]', "Write Your Review")
        self.your_name_input = Input(page, '//*[@id="name"]', "Your Name")
        self.email_address_input = Input(page, '//*[@id="email"]', "Email Address")
        self.add_review_input = Input(page, '//*[@id="review"]', "Add Review Here!")
        self.submit_button = Button(page, '//*[@id="button-review"]', "Submit")
        self.thank_you_review = Text(page, '//span[normalize-space()="Thank you for your review."]',
                                     "Thank you for your review.")

    def check_current_item(self):
        self.image_current_item.to_be_visible()
        self.image_current_item.to_have_attribute("src", "/get_product_picture/1")
        self.new_image.to_be_visible()
        self.new_image.to_have_attribute("src", "/static/images/product-details/new.jpg")
        self.item_title.to_be_visible()
        self.item_title.to_have_text("Blue Top")
        self.item_path.to_be_visible()
        self.item_path.to_have_text("Category: Women > Tops")
        self.stars_image.to_be_visible()
        self.stars_image.to_have_attribute("src", "/static/images/product-details/rating.png")
        self.price.to_be_visible()
        self.price.to_have_text("Rs. 500")
        self.quantity.to_be_visible()
        self.quantity.to_have_text("Quantity:")
        self.quantity_input.to_be_visible()
        self.quantity_input.to_have_attribute("value", "1")
        self.add_to_cart_button.to_be_visible()
        self.add_to_cart_button.to_have_text("Add to cart")
        self.add_to_cart_button.to_be_enabled()
        self.add_to_cart_icon.to_be_visible()
        self.add_to_cart_icon.to_have_class("fa fa-shopping-cart")
        self.availability_text.to_be_visible()
        self.availability_text.to_have_text("Availability: In Stock")
        self.condition_text.to_be_visible()
        self.condition_text.to_have_text("Condition: New")
        self.brand_text.to_be_visible()
        self.brand_text.to_have_text("Brand: Polo")

    def check_review_item(self):
        self.write_review_link.to_be_visible()
        self.write_review_link.to_have_text("Write Your Review")
        self.write_review_link.to_have_attribute("href", "#reviews")
        self.your_name_input.to_be_visible()
        self.your_name_input.to_have_attribute("placeholder", "Your Name")
        self.your_name_input.to_have_attribute("required", "")
        self.your_name_input.fill(self.fake.name())
        self.email_address_input.to_be_visible()
        self.email_address_input.to_have_attribute("placeholder", "Email Address")
        self.email_address_input.to_have_attribute("required", "")
        self.email_address_input.fill(self.fake.email())
        self.add_review_input.to_be_visible()
        self.add_review_input.to_have_attribute("placeholder", "Add Review Here!")
        self.add_review_input.to_have_attribute("required", "")
        self.add_review_input.fill(self.fake.text())
        self.submit_button.to_be_visible()
        self.submit_button.to_be_enabled()
        self.submit_button.click()
        self.thank_you_review.to_be_visible()
        self.thank_you_review.to_have_text("Thank you for your review.")
