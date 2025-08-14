from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.login_page.login_page import LoginPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.epic(AllureEpic.UI)
@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    @allure.story(AllureStory.SIGNUP)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Checking signup function")
    @pytest.mark.signup
    def test_signup(self, login_page:LoginPage):
        login_page.visit(urljoin(settings.app_url, "login"))
        login_page.signup.check_signup()
        login_page.signup.check_account_information()
        login_page.signup.check_address_information()
        login_page.signup.check_account_created()
    @allure.story(AllureStory.LOGIN)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Checking login function")
    @pytest.mark.login
    def test_login(self, login_page: LoginPage):
        login_page.visit(urljoin(settings.app_url, "login"))
        login_page.login.check_login()

