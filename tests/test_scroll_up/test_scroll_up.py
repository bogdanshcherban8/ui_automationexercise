from urllib.parse import urljoin

import allure
import pytest

from config import settings
from pages.cart_page.cart_page import CartPage
from pages.login_page.login_page import LoginPage
from pages.start_page.start_page import StartPage


@pytest.mark.scrollup
class TestScrollUp:
    @pytest.mark.smoke
    @pytest.mark.no_path
    @allure.title("Checking scroll up on static pages")
    @pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products"),
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
    def test_scroll_up_no_path(self, start_page: StartPage, url):
        start_page.visit(url)
        start_page.scroll_up.check_scroll_up()

    @pytest.mark.regression
    class TestScrollUpRegression:
        @allure.title("Checking scroll up on signup page")
        @pytest.mark.signup
        def test_scroll_up_signup_path(self, login_page:LoginPage):
            login_page.visit(urljoin(settings.app_url, "login"))
            login_page.signup.check_signup()
            login_page.scroll_up.check_scroll_up()

        @allure.title("Checking scroll up on cart")
        @pytest.mark.regression
        @pytest.mark.cart
        def test_lower_panel_cart_path(self, cart_page: CartPage):
            cart_page.visit(urljoin(settings.app_url, "login"))
            cart_page.login.check_login()
            cart_page.items.check_item()
            cart_page.items.added_item()
            cart_page.items.cart_item()
            cart_page.items.cart_item_continue()
            cart_page.scroll_up.check_scroll_up()