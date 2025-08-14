import re

import allure
from faker import Faker
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.input import Input
from components.elements.link import Link
from components.elements.text import Text


class Items(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.fake = Faker()
        self.item_image = Image(page, '//img[@src="/get_product_picture/1"]',
                                "Item image")
        self.price_title = Text(page,
                                '//div[@class="features_items"]//div[@class="productinfo text-center"]//h2[normalize-space()="Rs. 500"]',
                                "Rs. 500")
        self.item_title = Text(page,
                               '//div[@class="features_items"]//div[@class="productinfo text-center"]//p[normalize-space()="Blue Top"]',
                               "Blue Top")
        self.view_link = Link(page, '//a[@href="/product_details/1"]',
                              "View Product")
        self.view_icon = Icon(page, '//a[@href="/product_details/1"]//i[@class="fa fa-plus-square"]',
                              "fa fa-plus-square")
        self.add_to_cart = Text(page, '//section[2]//div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a',
                                "Add to cart")
        self.shopping_cart = Icon(page, '//section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a/i',
                                  "Shopping cart")
        self.overlay_price = Text(page, '//div[@class="overlay-content"]//h2[normalize-space()="Rs. 500"]',
                                  "Rs. 500")
        self.overlay_title = Text(page, '//div[@class="overlay-content"]//p[normalize-space()="Blue Top"]',
                                  "Blue Top")
        self.overlay_add_to_cart = Text(page,
                                        '//section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a',
                                        "Add to cart")
        self.overlay_shopping_cart = Icon(page,
                                          '//section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a/i',
                                          "Shopping cart")
        self.icon_box = Icon(page, '//i[normalize-space()=""]', "")
        self.added_title = Text(page, '//h4[normalize-space()="Added!"]', "Added!")
        self.your_product_text = Text(page, '//p[normalize-space()="Your product has been added to cart."]',
                                      "Your product has been added to cart.")
        self.continue_button = Button(page, '//button[normalize-space()="Continue Shopping"]', "Continue Shopping")
        self.view_cart_link = Link(page, '//p[@class="text-center"]//a[@href="/view_cart"]', "View Cart")
        self.item_title_box = Text(page,
                                   '//td[normalize-space()="Item"]', "Item")
        self.item_description_box = Text(page,
                                         '//td[normalize-space()="Description"]', "Description")
        self.item_price_box = Text(page,
                                   '//td[normalize-space()="Price"]', "Price")
        self.item_quantity_box = Text(page,
                                      '//td[normalize-space()="Quantity"]', "Quantity")
        self.item_total_box = Text(page,
                                   '//td[normalize-space()="Total"]', "total")
        self.item_image_box = Image(page, '//td[@class="cart_product"]//img', "Item image")
        self.item_title_link = Link(page, '//td[@class="cart_description"]//a', "Blue Top")
        self.item_description_text = Text(page, '//td[@class="cart_description"]//p', "Women > Tops")
        self.item_price_text = Text(page, '//td[@class="cart_price"]//p', "Rs. 500")
        self.item_quantity_button = Button(page, '//td[@class="cart_quantity"]/button', "1")
        self.item_total_text = Text(page,
                                    '//td[@class="cart_total"]/p',
                                    "Rs. 500")
        self.item_delete_button = Button(page, '//td[@class="cart_delete"]/a', "Delete button")
        self.item_delete_icon = Icon(page, '//i[@class="fa fa-times"]', "fa fa-times")
        self.proceed_button = Button(page, '//a[normalize-space()="Proceed To Checkout"]', "Proceed To Checkout")
        self.here_link = Link(page, '//a[normalize-space()="here"]', "Here")
        self.address_details_title = Text(page, '//h2[normalize-space()="Address Details"]', "Address Details")
        self.your_delivery_title = Text(page, '//h3[normalize-space()="Your delivery address"]',
                                        "Your delivery address")
        self.your_billing_title = Text(page, '//h3[normalize-space()="Your billing address"]', "Your billing address")
        self.review_title = Text(page, '//h2[normalize-space()="Review Your Order"]', "Review Your Order")
        self.total_amount = Text(page, '//tr[2]/td[3]/h4/b', "Total Amount")
        self.review_below_title = Text(page,
                                       '//label[normalize-space()="If you would like to add a comment about your order, please write it in the field below."]',
                                       "If you would like")
        self.textarea_review_input = Input(page, '//textarea[@name="message"]', "Textarea")
        self.place_order_link = Link(page, '//a[@href="/payment"]', "Place Order")
        self.total_price_title = Text(page, '//tr[2]/td[4]/p', "Rs. 500")
        self.payment_title = Text(page, '//h2[normalize-space()="Payment"]', "Payment")
        self.name_of_card_title = Text(page, '//label[normalize-space()="Name on Card"]', "Name on Card")
        self.name_of_card_input = Input(page, '//input[@data-qa="name-on-card"]', "Name on Card input")
        self.card_number_title = Text(page, '//label[normalize-space()="Card Number"]', "Card Number")
        self.card_number_input = Input(page, '//input[@data-qa="card-number"]', "Card Number input")
        self.cvc_title = Text(page, '//label[normalize-space()="CVC"]', "CVC")
        self.cvc_input = Input(page, '//input[@data-qa="cvc"]', "CVC input")
        self.expiration_title = Text(page, '//label[normalize-space()="Expiration"]', "Expiration")
        self.expiration_month_input = Input(page, '//input[@data-qa="expiry-month"]', "Month")
        self.expiration_year_input = Input(page, '//input[@data-qa="expiry-year"]', "Year")
        self.pay_order_button = Button(page, '//*[@id="submit"]', "Pay and Confirm Order")
        self.order_placed_title = Text(page, '//b[normalize-space()="Order Placed!"]', "Order placed!")
        self.congratulations_text = Text(page, '//p[normalize-space()="Congratulations! Your order has been confirmed!"]',
                                         "Congratulations! Your order has been confirmed!")
        self.invoice_link = Link(page, '//a[normalize-space()="Download Invoice"]', "Download Invoice")
        self.continue_link = Link(page, '//a[normalize-space()="Continue"]', "Continue")

    @allure.step("Checking item properties")
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
        self.view_icon.to_be_visible()
        self.view_icon.to_have_class("fa fa-plus-square")
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

    @allure.step("Checking added item functionality")
    def added_item(self):
        self.overlay_add_to_cart.click()
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
        self.check_url("view_cart")

    @allure.step("Checking item in the cart")
    def cart_item(self):
        self.item_title_box.to_be_visible()
        self.item_title_box.to_have_text("Item")
        self.item_description_box.to_be_visible()
        self.item_description_box.to_have_text("Description")
        self.item_price_box.to_be_visible()
        self.item_price_box.to_have_text("Price")
        self.item_quantity_box.to_be_visible()
        self.item_quantity_box.to_have_text("Quantity")
        self.item_total_box.to_be_visible()
        self.item_total_box.to_have_text("Total")
        self.item_image_box.to_be_visible()
        self.item_image_box.to_have_attribute("src", "get_product_picture/1")
        self.item_title_link.to_be_visible()
        self.item_title_link.to_have_text("Blue Top")
        self.item_title_link.to_have_attribute("href", "/product_details/1")
        self.item_description_text.to_be_visible()
        self.item_description_text.to_have_text("Women > Tops")
        self.item_price_text.to_be_visible()
        self.item_price_text.to_have_text("Rs. 500")
        self.item_quantity_button.to_be_visible()
        quantity = self.item_quantity_button.inner_text()
        delete_button = self.item_delete_button.is_visible()
        if quantity != "1" and delete_button:
            self.item_delete_button.click()
            self.here_link.click()
            self.item_image.hover()
            self.overlay_add_to_cart.click()
            self.view_cart_link.click()
        self.item_quantity_button.to_have_text("1")
        self.item_total_text.to_be_visible()
        self.item_total_text.to_have_text("Rs. 500")

    @allure.step("Clicking continue in cart page")
    def cart_item_continue(self):
        self.item_delete_button.to_be_visible()
        self.item_delete_button.to_be_enabled()
        self.item_delete_icon.to_be_visible()
        self.item_delete_icon.to_have_class("fa fa-times")
        self.proceed_button.to_be_visible()
        self.proceed_button.to_have_text("Proceed To Checkout")
        self.proceed_button.to_be_enabled()
        self.proceed_button.click()

    @allure.step("Checking checkout page functionality")
    def check_checkout(self):
        self.check_url("checkout")
        self.address_details_title.to_be_visible()
        self.address_details_title.to_have_text("Address Details")
        self.your_delivery_title.to_be_visible()
        self.your_delivery_title.to_have_text("Your delivery address")
        self.your_billing_title.to_be_visible()
        self.your_billing_title.to_have_text("Your billing address")
        self.review_title.to_be_visible()
        self.review_title.to_have_text("Review Your Order")
        self.cart_item()
        self.total_amount.to_be_visible()
        self.total_amount.to_have_text("Total Amount")
        self.total_price_title.to_be_visible()
        self.total_price_title.to_have_text("Rs. 500")
        self.review_below_title.to_be_visible()
        self.review_below_title.to_have_text(
            "If you would like to add a comment about your order, please write it in the field below.")
        self.textarea_review_input.to_be_visible()
        self.textarea_review_input.fill(self.fake.text())
        self.place_order_link.to_be_visible()
        self.place_order_link.to_have_text("Place Order")
        self.place_order_link.to_have_attribute("href", "/payment")
        self.place_order_link.click()

    @allure.step("Checking payment page functionality")
    def check_payment(self):
        self.check_url("payment")
        self.payment_title.to_be_visible()
        self.payment_title.to_have_text("Payment")
        self.name_of_card_title.to_be_visible()
        self.name_of_card_title.to_have_text("Name on Card")
        self.name_of_card_input.to_be_visible()
        self.name_of_card_input.to_have_attribute("required", "")
        self.name_of_card_input.fill(self.fake.credit_card_provider())
        self.card_number_title.to_be_visible()
        self.card_number_title.to_have_text("Card Number")
        self.card_number_input.to_be_visible()
        self.card_number_input.to_have_attribute("required", "")
        self.card_number_input.fill(self.fake.credit_card_number())
        self.cvc_title.to_be_visible()
        self.cvc_title.to_have_text("CVC")
        self.cvc_input.to_be_visible()
        self.cvc_input.to_have_attribute("required", "")
        self.cvc_input.fill(self.fake.credit_card_security_code())
        self.expiration_title.to_be_visible()
        self.expiration_title.to_have_text("Expiration")
        self.expiration_month_input.to_be_visible()
        self.expiration_month_input.to_have_attribute("required", "")
        self.expiration_month_input.fill(self.fake.credit_card_expire())
        self.expiration_year_input.to_be_visible()
        self.expiration_year_input.to_have_attribute("required", "")
        self.expiration_year_input.fill(self.fake.credit_card_expire())
        self.pay_order_button.to_be_visible()
        self.pay_order_button.to_have_text("Pay and Confirm Order")
        self.pay_order_button.to_be_enabled()
        self.pay_order_button.click()

    @allure.step("Checking that payment is done")
    def payment_done(self):
        self.order_placed_title.to_be_visible()
        self.order_placed_title.to_have_text("Order Placed!")
        self.congratulations_text.to_be_visible()
        self.congratulations_text.to_have_text("Congratulations! Your order has been confirmed!")
        self.invoice_link.to_be_visible()
        self.invoice_link.to_have_text("Download Invoice")
        self.invoice_link.to_have_attribute("href", "/download_invoice/500")
        with self.page.expect_download() as download_info:
            self.invoice_link.click()
        download = download_info.value
        path = download.path()
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        expected_text = "Hi 32 32, Your total purchase amount is 500. Thank you"
        assert expected_text in content, f"Текст '{expected_text}' не найден в файле"

        self.continue_link.to_be_visible()
        self.continue_link.to_have_text("Continue")
        self.continue_link.to_have_attribute("href", "/")
        self.continue_link.click()

    def check_url(self, text: str):
        self.check_current_url(re.compile(rf'.*/{text}'))
