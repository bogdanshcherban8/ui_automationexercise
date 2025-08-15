import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent

from components.elements.icon import Icon
from components.elements.image import Image
from components.elements.link import Link
from components.elements.text import Text
from config import settings


class Navbar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo_image = Image(page, '//img[@src="/static/images/home/logo.png"]', "Automation Exercise")
        self.home_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/"]', "Home")
        self.home_icon = Icon(page, '//i[@class="fa fa-home"]', "fa fa-home")
        self.products_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/products"]', "Products")
        self.products_icon = Icon(page, '//i[@class="material-icons card_travel"]',
                                  "material-icons card_travel")
        self.cart_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/view_cart"]', "Cart")
        self.cart_icon = Icon(page, '//div[@class="shop-menu pull-right"]//i[@class="fa fa-shopping-cart"]',
                              "fa fa-shopping-cart")
        self.logout_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/logout"]', "Logout")
        self.logout_icon = Icon(page, '//i[@class="fa fa-lock"]', "fa fa-lock")
        self.delete_account_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/delete_account"]',
                                        "Delete Account")
        self.delete_account_icon = Icon(page, '//i[@class="fa fa-trash-o"]', "fa fa-trash-o")
        self.signup_link = Link(page, '//div[@class="shop-menu pull-right"]//a[@href="/login"]', "Signup / Login")
        self.signup_icon = Icon(page, '//i[@class="fa fa-lock"]', "fa fa-lock")
        self.test_cases_link = Link(page,
                                    '//div[@class="shop-menu pull-right"]//a[@href="/test_cases"]',
                                    "Test Cases")
        self.test_cases_icon = Icon(page,
                                    '//a[@href="/test_cases"]//i[@class="fa fa-list"]',
                                    "fa fa-list")
        self.api_testing_link = Link(page,
                                     '//div[@class="shop-menu pull-right"]//a[@href="/api_list"]',
                                     "API Testing")
        self.api_testing_icon = Icon(page,
                                     '//div[@class="shop-menu pull-right"]//a[@href="/api_list"]//i[@class="fa fa-list"]',
                                     "fa fa-list")
        self.youtube_link = Link(page,
                                 '//div[@class="shop-menu pull-right"]//a[@href="https://www.youtube.com/c/AutomationExercise"]',
                                 "Video Tutorials")
        self.youtube_icon = Icon(page,
                                 '//i[@class="fa fa-youtube-play"]', "fa fa-youtube-play")
        self.contact_us_link = Link(page,
                                    '//div[@class="shop-menu pull-right"]//a[@href="/contact_us"]', "Contact us")
        self.contact_us_icon = Icon(page,
                                    '//i[@class="fa fa-envelope"]', "fa fa-envelope")
        self.logged_in_as_icon = Icon(page,
                                      '//i[@class="fa fa-user"]', "fa fa-user")
        self.logged_in_as_text = Text(page,
                                      '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a',
                                      " Logged in as ")
        self.account_deleted_title = Text(page, '//b[normalize-space()="Account Deleted!"]', "Account Deleted!")
        self.permanently_deleted_title = Text(page,
                                              '//p[normalize-space()="Your account has been permanently deleted!"]',
                                              "Your account has been permanently deleted!")
        self.you_can_create_title = Text(page,
                                         '//p[normalize-space()="You can create new account to take advantage of member privileges to enhance your online shopping experience with us."]',
                                         "You can create new account")
        self.continue_link = Link(page, '//a[normalize-space()="Continue"]', "Continue")

    @allure.step("Checking navbar on static pages")
    def check_navbar_no_login(self):
        self.logo_image.to_be_visible()
        self.logo_image.to_have_attribute("src", "/static/images/home/logo.png")
        self.home_icon.to_be_visible()
        self.home_icon.to_have_class("fa fa-home")
        self.home_link.to_be_visible()
        self.home_link.to_have_text("Home")
        self.home_link.to_have_attribute("href", "/")
        self.products_icon.to_be_visible()
        self.products_icon.to_have_class("material-icons card_travel")
        self.products_link.to_be_visible()
        self.products_link.to_have_text(" Products")
        self.products_link.to_have_attribute("href", "/products")
        self.cart_icon.to_be_visible()
        self.cart_icon.to_have_class("fa fa-shopping-cart")
        self.cart_link.to_be_visible()
        self.cart_link.to_have_text("Cart")
        self.cart_link.to_have_attribute("href", "/view_cart")
        self.test_cases_icon.to_be_visible()
        self.test_cases_icon.to_have_class("fa fa-list")
        self.test_cases_link.to_be_visible()
        self.test_cases_link.to_have_text("Test Cases")
        self.test_cases_link.to_have_attribute("href", "/test_cases")
        self.api_testing_icon.to_be_visible()
        self.api_testing_icon.to_have_class("fa fa-list")
        self.api_testing_link.to_be_visible()
        self.api_testing_link.to_have_text("API Testing")
        self.api_testing_link.to_have_attribute("href", "/api_list")
        self.youtube_icon.to_be_visible()
        self.youtube_icon.to_have_class("fa fa-youtube-play")
        self.youtube_link.to_be_visible()
        self.youtube_link.to_have_text("Video Tutorials")
        self.youtube_link.to_have_attribute("href", "https://www.youtube.com/c/AutomationExercise")
        self.contact_us_icon.to_be_visible()
        self.contact_us_icon.to_have_class("fa fa-envelope")
        self.contact_us_link.to_be_visible()
        self.contact_us_link.to_have_text("Contact us")
        self.contact_us_link.to_have_attribute("href", "/contact_us")

    @allure.step("Checking signup / login button")
    def check_signup(self):
        self.signup_icon.to_be_visible()
        self.signup_icon.to_have_class("fa fa-lock")
        self.signup_link.to_be_visible()
        self.signup_link.to_have_text("Signup / Login")
        self.signup_link.to_have_attribute("href", "/login")

    @allure.step("Checking navbar with authorized user")
    def check_navbar_with_login(self):
        self.check_navbar_no_login()
        self.delete_account_icon.to_be_visible()
        self.delete_account_icon.to_have_class("fa fa-trash-o")
        self.delete_account_link.to_be_visible()
        self.delete_account_link.to_have_text("Delete Account")
        self.delete_account_link.to_have_attribute("href", "/delete_account")
        self.logout_icon.to_be_visible()
        self.logout_icon.to_have_class("fa fa-lock")
        self.logout_link.to_be_visible()
        self.logout_link.to_have_text("Logout")
        self.logout_link.to_have_attribute("href", "/logout")
        self.logged_in_as_icon.to_be_visible()
        self.logged_in_as_icon.to_have_class("fa fa-user")
        self.logged_in_as_text.to_be_visible()

    @allure.step("Checking logout function")
    def check_navbar_logout_login(self):
        self.logout_link.click()
        self.check_navbar_no_login()
        self.check_signup()

    @allure.step("Checking delete account function")
    def check_navbar_delete_login(self):
        self.delete_account_link.click()
        self.account_deleted_title.to_be_visible()
        self.account_deleted_title.to_have_text("Account Deleted!")
        self.permanently_deleted_title.to_be_visible()
        self.permanently_deleted_title.to_have_text("Your account has been permanently deleted!")
        self.you_can_create_title.to_be_visible()
        self.you_can_create_title.to_have_text(
            "You can create new account to take advantage of member privileges to enhance your online shopping experience with us.")
        self.continue_link.to_be_visible()
        self.continue_link.to_have_text("Continue")
        self.continue_link.to_have_attribute("href", "/")
        self.continue_link.click()
        self.check_navbar_no_login()
        self.check_signup()
