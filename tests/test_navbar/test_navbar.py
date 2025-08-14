from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.cart_page.cart_page import CartPage
from pages.login_page.login_page import LoginPage
from pages.start_page.start_page import StartPage

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.NAVBAR)
@allure.epic(AllureEpic.UI)
@allure.story(AllureStory.NAVBAR)
@allure.severity(Severity.NORMAL)
@pytest.mark.navbar
class TestNavbar:
    @allure.title("Checking navbar on static pages")
    @pytest.mark.smoke
    @pytest.mark.no_path
    @pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products"),
                                     urljoin(settings.app_url, "view_cart"), urljoin(settings.app_url, "login"),
                                     urljoin(settings.app_url, "test_cases"), urljoin(settings.app_url, "api_list"),
                                     urljoin(settings.app_url, "contact_us"),
                                     urljoin(settings.app_url, "category_products/1"),
                                     urljoin(settings.app_url, "category_products/2"),
                                     urljoin(settings.app_url, "category_products/7"),
                                     urljoin(settings.app_url, "category_products/3"),
                                     urljoin(settings.app_url, "category_products/6"),
                                     urljoin(settings.app_url, "category_products/4"),
                                     urljoin(settings.app_url, "category_products/5"),
                                     urljoin(settings.app_url, "brand_products/Polo"),
                                     urljoin(settings.app_url, "brand_products/H&M"),
                                     urljoin(settings.app_url, "brand_products/Madame"),
                                     urljoin(settings.app_url, "brand_products/Mast%20&%20Harbour"),
                                     urljoin(settings.app_url, "brand_products/Babyhug"),
                                     urljoin(settings.app_url, "brand_products/Allen%20Solly%20Junior"),
                                     urljoin(settings.app_url, "brand_products/Kookie%20Kids"),
                                     urljoin(settings.app_url, "brand_products/Biba"),
                                     urljoin(settings.app_url, "product_details/1")])
    def test_navbar_no_login(self, start_page: StartPage, url):
        start_page.visit(url)
        start_page.navbar.check_navbar_no_login()
        start_page.navbar.check_signup()

    @pytest.mark.regression
    class TestNavbarRegression:
        @allure.title("Checking navbar panel on signup page")
        @pytest.mark.signup
        def test_navbar_signup_path(self, login_page: LoginPage):
            login_page.visit(urljoin(settings.app_url, "login"))
            login_page.signup.check_signup()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_account_information()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_address_information()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_account_created()
            login_page.navbar.check_navbar_with_login()

        @allure.title("Checking navbar on cart")
        @pytest.mark.cart
        def test_navbar_cart_path(self, cart_page: CartPage):
            cart_page.visit(urljoin(settings.app_url, "login"))
            cart_page.navbar.check_navbar_no_login()
            cart_page.navbar.check_signup()
            cart_page.login.check_login()
            cart_page.navbar.check_navbar_with_login()
            cart_page.items.check_item()
            cart_page.items.added_item()
            cart_page.navbar.check_navbar_with_login()
            cart_page.items.cart_item()
            cart_page.items.cart_item_continue()
            cart_page.navbar.check_navbar_with_login()
            cart_page.items.check_checkout()
            cart_page.navbar.check_navbar_with_login()
            cart_page.items.check_payment()
            cart_page.navbar.check_navbar_with_login()
            cart_page.items.payment_done()

        @allure.title("Checking navbar logout and delete account")
        @pytest.mark.signup
        def test_navbar_logout_delete_account(self, login_page: LoginPage):
            login_page.visit(urljoin(settings.app_url, "login"))
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.login.check_login()
            login_page.navbar.check_navbar_with_login()
            login_page.navbar.check_navbar_logout_login()
            login_page.visit(urljoin(settings.app_url, "login"))
            login_page.signup.check_signup()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_account_information()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_address_information()
            login_page.navbar.check_navbar_no_login()
            login_page.navbar.check_signup()
            login_page.signup.check_account_created()
            login_page.navbar.check_navbar_with_login()
            login_page.navbar.check_navbar_delete_login()
