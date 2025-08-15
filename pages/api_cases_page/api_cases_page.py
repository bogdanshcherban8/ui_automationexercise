from playwright.sync_api import Page

from components.api_cases.api_cases import ApiCases
from pages.base_page import BasePage


class ApiCasesPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.api_cases=ApiCases(page)