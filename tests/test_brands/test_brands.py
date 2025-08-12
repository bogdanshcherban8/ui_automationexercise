from urllib.parse import urljoin

import allure
import pytest

from config import settings
from pages.start_page.start_page import StartPage
@pytest.mark.brands
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking brands on static pages")
@pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products"), urljoin(settings.app_url, "product_details/1")])
def test_brands_no_path(start_page:StartPage, url):
    start_page.visit(url)
    start_page.brands.check_brands_title()
    start_page.brands.check_brands()