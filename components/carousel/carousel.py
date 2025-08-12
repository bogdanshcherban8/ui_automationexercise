from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.image import Image
from components.elements.text import Text


class Carousel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.automation_text = Text(page,
                                    '//div[@class="item active"]//h1[normalize-space()="AutomationExercise"]',
                                    "Automation Exercise")
        self.practice_text = Text(page,
                                  '//div[@class="item active"]//h2[normalize-space()="Full-Fledged practice website for Automation Engineers"]',
                                  "Full-Fledged practice")
        self.qa_text = Text(page,
                            '//div[@class="item active"]//p[normalize-space()="All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills."]',
                            "All QA engineers")
        self.test_cases_button = Button(page, '//div[@class="item active"]//a[@href="/test_cases"]', "Test Cases")
        self.api_list_button = Button(page, '//div[@class="item active"]//a[@href="/api_list"]',
                                      "APIs list for practice")
        self.three_low_buttons = Button(page, '//li[@class="active"]', "Low buttons")
        self.left_button = Button(page, '//a[@class="left control-carousel hidden-xs"]', "Left button")
        self.right_button = Button(page, '//a[@class="right control-carousel hidden-xs"]', "Right button")
        self.image = Image(page, '//div[@class="item active"]//img[@class="girl img-responsive"]', "image")
        self.features_items = Text(page, '//h2[normalize-space()="Features Items"]', "Features Items")

    def check_carousel_block(self):
        self.automation_text.to_be_visible()
        self.automation_text.to_have_text("AutomationExercise")
        self.practice_text.to_be_visible()
        self.practice_text.to_have_text("Full-Fledged practice website for Automation Engineers")
        self.qa_text.to_be_visible()
        self.qa_text.to_contain_text(
            "All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills.")
        self.test_cases_button.to_be_visible()
        self.test_cases_button.to_have_attribute("href", "/test_cases")
        self.test_cases_button.to_have_text("Test Cases")
        self.test_cases_button.to_be_enabled()
        self.api_list_button.to_be_visible()
        self.api_list_button.to_have_attribute("href", "/api_list")
        self.api_list_button.to_have_text("APIs list for practice")
        self.api_list_button.to_be_enabled()
        self.three_low_buttons.to_be_visible()

    def check_carousel(self):
        self.check_carousel_block()
        self.image.to_be_visible()
        self.image.to_have_attribute("src", "/static/images/home/girl2.jpg")
        self.left_button.to_be_visible()
        self.left_button.to_have_attribute("href", "#slider-carousel")
        self.right_button.to_be_visible()
        self.right_button.to_have_attribute("href", "#slider-carousel")
        self.right_button.click()
        self.check_carousel_block()
        self.image.to_be_visible()
        self.image.to_have_attribute("src", "/static/images/home/girl1.jpg")
        self.right_button.click()
        self.check_carousel_block()
        self.image.to_be_visible()
        self.image.to_have_attribute("src", "/static/images/home/girl3.jpg")
        self.features_items.to_be_visible()
        self.features_items.to_have_text("Features Items")
