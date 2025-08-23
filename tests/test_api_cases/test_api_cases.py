from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.api_cases_page.api_cases_page import ApiCasesPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

api_data = [(urljoin(settings.app_url, "api_list"), "APIs List for practice",
             "Below is the list of APIs for you to practice the API testing in Automation. Click on the scenario for detailed API:",
             "API 1: Get All Products List", "API URL: https://automationexercise.com/api/productsList")]
test_data = [(urljoin(settings.app_url, "test_cases"), "Test Cases",
              "Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:",
             "Test Case 1: Register User", "1. Launch browser")]
@allure.feature(AllureFeature.API_CASES)
@allure.epic(AllureEpic.UI)
@allure.severity(Severity.TRIVIAL)
@pytest.mark.no_path
@pytest.mark.smoke
@pytest.mark.api_cases
@pytest.mark.flacky(rerun=3, delay=2)
class TestApiCases:
    @allure.story(AllureStory.API_TESTING)
    @allure.title("Checking api testing page")
    @pytest.mark.parametrize("url, title_text, description, collapse, item", api_data)
    def test_api_no_path(self, api_cases_page: ApiCasesPage, url, title_text, description, collapse, item):
        api_cases_page.visit(url)
        api_cases_page.api_cases.check_api_cases(title_text, description, collapse, item)

    @allure.story(AllureStory.TEST_CASES)
    @allure.title("Checking test cases page")
    @pytest.mark.parametrize("url, title_text, description, collapse, item", test_data)
    def test_cases_no_path(self, api_cases_page: ApiCasesPage, url, title_text, description, collapse, item):
        api_cases_page.visit(url)
        api_cases_page.api_cases.check_api_cases(title_text, description, collapse, item)
