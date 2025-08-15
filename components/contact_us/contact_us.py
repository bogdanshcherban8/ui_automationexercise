import re

import allure
from faker import Faker
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.input import Input
from components.elements.input_file import InputFile
from components.elements.link import Link
from components.elements.text import Text
from config import settings


class ContactUs(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.fake = Faker()
        self.title_text = Text(page, '//h2[normalize-space()="Contact Us"]', "Contact Us")
        self.note_text = Text(page, '//div[@class="contact-form"]/div[1]', "Note: Below contact form is for testing purpose.")
        self.get_in_touch_text = Text(page, '//h2[normalize-space()="Get In Touch"]', "Get In Touch")
        self.feedback_for_us_text = Text(page, '//h2[normalize-space()="Feedback For Us"]', "Feedback For Us")
        self.we_really_text = Text(page, '//p[normalize-space()="We really appreciate your response to our website."]',
                                   "We really")
        self.kindly_text = Text(page,
                                '//p[normalize-space()="Kindly share your feedback with us at feedback@automationexercise.com."]',
                                "Kindly share")
        self.feedback_mail = Link(page, '//a[@href="mailto:feedback@automationexercise.com"]',
                                  "mailto:feedback@automationexercise.com")
        self.if_you_have_text = Text(page,
                                     '//p[normalize-space()="If you have any suggestion areas or improvements, do let us know. We will definitely work on it."]',
                                     "If you have")
        self.thank_text = Text(page, '//p[normalize-space()="Thank you"]', "Thank you")
        self.name_input = Input(page, '//input[@data-qa="name"]', "Name")
        self.email_input = Input(page, '//input[@data-qa="email"]', "Email")
        self.subject_input = Input(page, '//input[@data-qa="subject"]', "Subject")
        self.your_message_input = Input(page, '//textarea[@data-qa="message"]', "Your Message Here")
        self.submit_button = Button(page, '//input[@data-qa="submit-button"]', "Submit")
        self.input_file = InputFile(page, '//input[@name="upload_file"]', "Choose File")
        self.success_text = Text(page,
                                 '//div[@class="status alert alert-success"]',"Success!")
        self.home_button = Button(page, '//span[normalize-space()="Home"]', "Home")
        self.home_icon = Icon(page, '//i[@class="fa fa-angle-double-left"]', "<<")

    @allure.step("Checking contact us page functionality")
    def check_contact_us(self):
        self.title_text.to_be_visible()
        self.title_text.to_have_text("Contact Us")
        self.note_text.to_be_visible()
        self.note_text.to_have_text("Note: Below contact form is for testing purpose.")
        self.get_in_touch_text.to_be_visible()
        self.get_in_touch_text.to_have_text("Get In Touch")
        self.feedback_for_us_text.to_be_visible()
        self.feedback_for_us_text.to_have_text("Feedback For Us")
        self.we_really_text.to_be_visible()
        self.we_really_text.to_have_text("We really appreciate your response to our website.")
        self.kindly_text.to_be_visible()
        self.kindly_text.to_have_text("Kindly share your feedback with us at feedback@automationexercise.com.")
        self.feedback_mail.to_be_visible()
        self.feedback_mail.to_have_text("feedback@automationexercise.com")
        self.feedback_mail.to_have_attribute("href", "mailto:feedback@automationexercise.com")
        self.if_you_have_text.to_be_visible()
        self.if_you_have_text.to_have_text(
            "If you have any suggestion areas or improvements, do let us know. We will definitely work on it.")
        self.thank_text.to_be_visible()
        self.thank_text.to_have_text("Thank you")
        self.name_input.to_be_visible()
        self.name_input.to_have_attribute("placeholder", "Name")
        self.name_input.fill(self.fake.name())
        self.email_input.to_be_visible()
        self.email_input.to_have_attribute("placeholder", "Email")
        self.email_input.fill(self.fake.email())
        self.subject_input.to_be_visible()
        self.subject_input.to_have_attribute("placeholder", "Subject")
        self.subject_input.fill(self.fake.sentence())
        self.your_message_input.to_be_visible()
        self.your_message_input.to_have_attribute("placeholder", "Your Message Here")
        self.your_message_input.fill(self.fake.text())
        self.submit_button.to_be_visible()
        self.submit_button.to_have_attribute("value", "Submit")
        self.input_file.to_be_visible()
        self.input_file.set_input_files(settings.input_file)
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
        self.success_text.to_be_visible()
        self.success_text.to_have_text("Success! Your details have been submitted successfully.")
        self.home_button.to_be_visible()
        self.home_button.to_have_text("Home")
        self.home_icon.to_be_visible()
        self.home_icon.to_have_class("fa fa-angle-double-left")
        self.home_button.click()
        self.check_url("")

    def check_url(self, text: str):
        self.check_current_url(re.compile(rf'.*/{text}'))
