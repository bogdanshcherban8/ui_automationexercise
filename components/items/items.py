import re

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
        self.fake=Faker()
        self.item_image = Image(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/img',
                                "Item image")
        self.price_title = Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/h2',
                                "Rs. 500")
        self.item_title = Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/p',
                               "Blue Top")
        self.view_link = Link(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a',
                              "View Product")
        self.add_to_cart = Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a',
                                "Add to cart")
        self.shopping_cart = Icon(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a/i',
                                  "Shopping cart")
        self.overlay_price = Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/h2',
                                  "Rs. 500")
        self.overlay_title = Text(page, '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/p',
                                  "Blue Top")
        self.overlay_add_to_cart = Text(page,
                                        '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a',
                                        "Add to cart")
        self.overlay_shopping_cart = Icon(page,
                                          '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a/i',
                                          "Shopping cart")
        self.icon_box = Icon(page, '//*[@id="cartModal"]/div/div/div[1]/div/i', "")
        self.added_title = Text(page, '//*[@id="cartModal"]/div/div/div[1]/h4', "Added!")
        self.your_product_text = Text(page, '//*[@id="cartModal"]/div/div/div[2]/p[1]',
                                      "Your product has been added to cart.")
        self.continue_button = Button(page, '//*[@id="cartModal"]/div/div/div[3]/button', "Continue Shopping")
        self.view_cart_link = Link(page, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a', "View Cart")
        self.item_title_box = Text(page,
                                   '//*[@id="cart_info_table"]/thead/tr/td[1] | //*[@id="cart_info"]/table/thead/tr/td[1]',
                                   "Item")
        self.item_description_box = Text(page,
                                         '//*[@id="cart_info_table"]/thead/tr/td[2] | //*[@id="cart_info"]/table/thead/tr/td[2]',
                                         "Description")
        self.item_price_box = Text(page,
                                   '//*[@id="cart_info_table"]/thead/tr/td[3] | //*[@id="cart_info"]/table/thead/tr/td[3]',
                                   "Price")
        self.item_quantity_box = Text(page,
                                      '//*[@id="cart_info_table"]/thead/tr/td[4] | //*[@id="cart_info"]/table/thead/tr/td[4]',
                                      "Quantity")
        self.item_total_box = Text(page,
                                   '//*[@id="cart_info_table"]/thead/tr/td[5] | //*[@id="cart_info"]/table/thead/tr/td[5]',
                                   "total")
        self.item_image_box = Image(page, '//*[@id="product-1"]/td[1]/a/img', "Item image")
        self.item_title_link = Link(page, '//*[@id="product-1"]/td[2]/h4/a', "Blue Top")
        self.item_description_text = Text(page, '//*[@id="product-1"]/td[2]/p', "Women > Tops")
        self.item_price_text = Text(page, '//*[@id="product-1"]/td[3]/p', "Rs. 500")
        self.item_quantity_button = Button(page, '//*[@id="product-1"]/td[4]/button', "1")
        self.item_total_text = Text(page,
                                    '//*[@id="product-1"]/td[5]/p',
                                    "Rs. 500")
        self.item_delete_button = Button(page, '//*[@id="product-1"]/td[6]/a', "Delete button")
        self.item_delete_icon = Icon(page, '//*[@id="product-1"]/td[6]/a/i', "fa fa-times")
        self.proceed_button = Button(page, '//*[@id="do_action"]/div[1]/div/div/a', "Proceed To Checkout")
        self.here_link = Link(page, '//*[@id="empty_cart"]/p/a', "Here")
        self.address_details_title = Text(page, '//*[@id="cart_items"]/div/div[2]/h2', "Address Details")
        self.your_delivery_title = Text(page, '//*[@id="address_delivery"]/li[1]/h3', "Your Delivery Address")
        self.your_billing_title = Text(page, '//*[@id="address_invoice"]/li[1]/h3', "Your Billing Address")
        self.review_title = Text(page, '//*[@id="cart_items"]/div/div[4]/h2', "Review Your Order")
        self.total_amount = Text(page, '//*[@id="cart_info"]/table/tbody/tr[2]/td[3]/h4/b', "Total Amount")
        self.review_below_title = Text(page, '//*[@id="ordermsg"]/label',
                                       "If you would like to add a comment about your order, please write it in the field below.")
        self.textarea_review_input=Input(page, '//*[@id="ordermsg"]/textarea', "Textarea")
        self.place_order_link=Link(page, '//*[@id="cart_items"]/div/div[7]/a', "Place Order")
        self.total_price_title=Text(page, '//*[@id="cart_info"]/table/tbody/tr[2]/td[4]/p', "Rs. 500")
        self.payment_title=Text(page, '//*[@id="cart_items"]/div/div[2]/h2', "Payment")
        self.name_of_card_title=Text(page, '//*[@id="payment-form"]/div[1]/div/label', "Name of Card")
        self.name_of_card_input=Input(page, '//*[@id="payment-form"]/div[1]/div/input', "Name of Card input")
        self.card_number_title=Text(page, '//*[@id="payment-form"]/div[2]/div/label', "Card Number")
        self.card_number_input=Input(page, '//*[@id="payment-form"]/div[2]/div/input', "Card Number input")
        self.cvc_title=Text(page, '//*[@id="payment-form"]/div[3]/div[1]/label', "CVC")
        self.cvc_input=Input(page, '//*[@id="payment-form"]/div[3]/div[1]/input', "CVC input")
        self.expiration_title=Text(page, '//*[@id="payment-form"]/div[3]/div[2]/label', "Expiration")
        self.expiration_month_input=Input(page, '//*[@id="payment-form"]/div[3]/div[2]/input', "Month")
        self.expiration_year_input = Input(page, '//*[@id="payment-form"]/div[3]/div[3]/input', "Year")
        self.pay_order_button=Button(page, '//*[@id="submit"]', "Pay and Confirm Order")
        self.order_placed_title=Text(page, '//*[@id="form"]/div/div/div/h2/b', "Order placed!")
        self.congratulations_text=Text(page, '//*[@id="form"]/div/div/div/p', "Congratulations! Your order has been confirmed!")
        self.invoice_link=Link(page, '//*[@id="form"]/div/div/div/a', "Download Invoice")
        self.continue_link=Link(page, '//*[@id="form"]/div/div/div/div/a', "Continue")
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
        self.check_url("view_cart")

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
        delete_button=self.item_delete_button.is_visible()
        if quantity != "1" and delete_button:
            self.item_delete_button.click()
            self.here_link.click()
            self.item_image.hover()
            self.overlay_add_to_cart.click()
            self.view_cart_link.click()
        self.item_quantity_button.to_have_text("1")
        self.item_total_text.to_be_visible()
        self.item_total_text.to_have_text("Rs. 500")
    def cart_item_continue(self):
        self.item_delete_button.to_be_visible()
        self.item_delete_button.to_be_enabled()
        self.item_delete_icon.to_be_visible()
        self.item_delete_icon.to_have_class("fa fa-times")
        self.proceed_button.to_be_visible()
        self.proceed_button.to_have_text("Proceed To Checkout")
        self.proceed_button.to_be_enabled()
        self.proceed_button.click()

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
        self.review_below_title.to_have_text("If you would like to add a comment about your order, please write it in the field below.")
        self.textarea_review_input.to_be_visible()
        self.textarea_review_input.fill(self.fake.text())
        self.place_order_link.to_be_visible()
        self.place_order_link.to_have_text("Place Order")
        self.place_order_link.to_have_attribute("href", "/payment")
        self.place_order_link.click()
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
