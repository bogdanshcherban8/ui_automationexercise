from urllib.parse import urljoin

import allure
import pytest

from config import settings
from pages.start_page.start_page import StartPage
@pytest.mark.category
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking category on static pages")
@pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products"), urljoin(settings.app_url, "product_details/1")])
def test_category_no_path(start_page:StartPage, url):
    start_page.visit(url)
    start_page.category.check_category_title()
    start_page.category.check_category_women()
    start_page.category.check_category_men()
    start_page.category.check_category_kids()