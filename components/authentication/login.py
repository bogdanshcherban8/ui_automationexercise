import re

import allure
from faker import Faker
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.input import Input
from components.elements.text import Text
from config import settings


class Login(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.fake=Faker()
        self.login_title = Text(page, '//h2[normalize-space()="Login to your account"]', "Login to your account")
        self.email_input = Input(page, '//*[@id="form"]//input[@data-qa="login-email"]', "Email Address")
        self.password_input=Input(page, '//*[@id="form"]//input[@data-qa="login-password"]', "Password")
        self.wrong_data_alert = Text(page, '//p[normalize-space()="Your email or password is incorrect!"]',
                                        "Your email or password is incorrect!")
        self.login_button = Button(page, '//*[@id="form"]//button[@data-qa="login-button"]', "Login")
    @allure.step("Fill login form")
    def check_login(self):
        self.check_url('login')
        self.login_title.to_be_visible()
        self.login_title.to_have_text("Login to your account")
        self.email_input.to_be_visible()
        self.email_input.to_have_attribute("placeholder", "Email Address")
        self.email_input.fill(self.fake.email())
        self.email_input.to_have_attribute("required", "")
        self.password_input.to_be_visible()
        self.password_input.to_have_attribute("placeholder", "Password")
        self.password_input.fill(self.fake.password())
        self.password_input.to_have_attribute("required", "")
        self.login_button.to_be_visible()
        self.login_button.to_be_enabled()
        self.login_button.click()
        alert_visible = False
        try:
            self.wrong_data_alert.wait_for()
            alert_visible = True
        except:
            pass

        if alert_visible:
            self.email_input.fill(settings.test_user.email)
            self.password_input.fill(settings.test_user.password)
            self.login_button.click()
        self.check_url("")

    def check_url(self, text: str):
        self.check_current_url(re.compile(rf'.*/{text}'))