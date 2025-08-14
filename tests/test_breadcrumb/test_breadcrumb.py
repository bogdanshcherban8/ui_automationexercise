from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.cart_page.cart_page import CartPage
from pages.products_page.products_page import ProductsPage

products_data = ["Women > Dress", "Women > Tops", "Women > Saree", "Men > Tshirts", "Men > Jeans", "Kids > Dress",
                 "Kids > Tops & Shirts", "Polo", "H&M", "Madame", "Mast & Harbour", "Babyhug", "Allen Solly Junior",
                 "Kookie Kids", "Biba"]
urls = [urljoin(settings.app_url, "category_products/1"),
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
        urljoin(settings.app_url, "brand_products/Biba")]
url_cart=[urljoin(settings.app_url, "view_cart"), urljoin(settings.app_url, "checkout"), urljoin(settings.app_url, "payment")]
cart_text=["Shopping Cart", "Checkout", "Payment"]

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.BREADCRUMB)
@allure.epic(AllureEpic.UI)
@allure.severity(Severity.TRIVIAL)
@allure.story(AllureStory.BREADCRUMB)
@pytest.mark.breadcrumb
class TestBreadcrumb:
    @pytest.mark.smoke
    @pytest.mark.no_path
    @allure.title("Checking breadcrumb on static pages")
    @pytest.mark.parametrize("url, path_text", zip(urls,products_data))
    def test_breadcrumb_no_path(self,products_page: ProductsPage, url, path_text):
        products_page.visit(url)
        products_page.breadcrumb.check_breadcrumb_products(path_text)
    @pytest.mark.parametrize("url_cart, cart_text", zip(url_cart, cart_text))
    @pytest.mark.regression
    @allure.title("Checking breadcrumb on cart page")
    @pytest.mark.cart
    def test_breadcrumb_cart(self, cart_page:CartPage, url_cart, cart_text):
        cart_page.visit(urljoin(settings.app_url, "login"))
        cart_page.login.check_login()
        cart_page.visit(url_cart)
        cart_page.breadcrumb.check_breadcrumb_products(cart_text)