from faker import Faker
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.input import Input
from components.elements.text import Text


class SubscriptionCopyright(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.fake = Faker()
        self.subscription_title = Text(page, '//*[@id="footer"]/div[1]/div/div/div[2]/div/h2', "Subscription")
        self.email_input = Input(page, '//*[@id="susbscribe_email"]', "Your email address")
        self.subscribe_button = Button(page, '//*[@id="subscribe"]', "Subscribe")
        self.subscribe_button_icon = Icon(page, '//*[@id="subscribe"]/i', "fa fa-arrow-circle-o-right")
        self.two_low_paragraphs = Text(page, '//*[@id="footer"]/div[1]/div/div/div[2]/div/form/p',
                                       "Get the most recent updates from our site and be updated your self...")
        self.copyright_text=Text(page, '//*[@id="footer"]/div[2]/div/div/p', "Copyright © 2021 All rights reserved")
        self.subscribe_alert=Text(page, '//*[@id="success-subscribe"]/div', "You have been successfully subscribed!")
    def check_subscription_copyright(self):
        self.subscription_title.to_be_visible()
        self.subscription_title.to_have_text("Subscription")
        self.email_input.to_be_visible()
        self.email_input.to_have_attribute("placeholder", "Your email address")
        self.email_input.fill(self.fake.email())
        self.subscribe_button.to_be_visible()
        self.subscribe_button.to_be_enabled()
        self.subscribe_button_icon.to_have_class("fa fa-arrow-circle-o-right")
        self.two_low_paragraphs.to_be_visible()
        self.two_low_paragraphs.to_have_text("Get the most recent updates from our site and be updated your self...")
        self.copyright_text.to_be_visible()
        self.copyright_text.to_have_text("Copyright © 2021 All rights reserved")
        self.subscribe_button.click()
        self.subscribe_alert.to_be_visible()
        self.subscribe_alert.to_have_text("You have been successfully subscribed!")
