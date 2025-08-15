from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.elements.link import Link
from components.elements.text import Text
import allure

class ApiCases(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.main_title = Text(page, '//*[@id="form"]//h2/b', "main title")
        self.description = Text(page, '//*[@id="form"]//h5/span', "description")
        self.collapse_1 = Link(page, '//*[@id="form"]//a[@href="#collapse1"]', "collapse 1")
        self.list_item_1 = Text(page, '//*[@id="collapse1"]/ul/li[1]', "list-group-item")
        self.feedback_link = Link(page, '//a[normalize-space()="Feedback for Us"]', "Feedback for Us")
        self.text_1 = Text(page, '//li[normalize-space()="We have identified above scenarios and added in the list."]',
                           "We have identified...")
        self.text_2 = Text(page,
                           '//li[normalize-space()="You can explore more test cases in the website and if you find new test scenario that is not covered in above list, do let us know. We will definitely add that in above list."]',
                           "You can explore...")
        self.text_3 = Text(page, '//li[normalize-space()="If you think, this website should cover up any particular feature, kindly share with us at feedback@automationexercise.com. We will work on that part. Your feedback matters a lot."]',
                           "If you think...")
        self.link_1 = Link(page, '//a[normalize-space()="feedback@automationexercise.com"]', "feedback@automationexercise.com")
    @allure.step("Checking api and test cases page functionality")
    def check_api_cases(self, title_text: str, description: str, collapse: str, item: str):
        self.main_title.to_be_visible()
        self.main_title.to_have_text(title_text)
        self.description.to_be_visible()
        self.description.to_have_text(description)
        self.collapse_1.to_be_visible()
        self.collapse_1.to_have_attribute("href", "#collapse1")
        self.collapse_1.to_have_text(collapse)
        self.collapse_1.click()
        self.list_item_1.to_be_visible()
        self.list_item_1.to_have_text(item)
        self.feedback_link.to_be_visible()
        self.feedback_link.to_have_attribute("href", "#feedback")
        self.feedback_link.to_have_text("Feedback for Us")
        self.text_1.to_be_visible()
        self.text_1.to_have_text("We have identified above scenarios and added in the list.")
        self.text_2.to_be_visible()
        self.text_2.to_have_text(
            "You can explore more test cases in the website and if you find new test scenario that is not covered in above list, do let us know. We will definitely add that in above list.")
        self.text_3.to_be_visible()
        self.text_3.to_have_text(
            "If you think, this website should cover up any particular feature, kindly share with us at feedback@automationexercise.com. We will work on that part. Your feedback matters a lot.")
        self.link_1.to_be_visible()
        self.link_1.to_have_text("feedback@automationexercise.com")
        self.link_1.to_have_attribute("href", "mailto:feedback@automationexercise.com")
