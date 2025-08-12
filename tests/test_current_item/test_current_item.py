from urllib.parse import urljoin

import allure
import pytest

from config import settings
from pages.products_page.products_page import ProductsPage
@pytest.mark.current_item
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking current item on static page")
def test_current_item_no_path(products_page:ProductsPage):
    products_page.visit(urljoin(settings.app_url, "product_details/1"))
    products_page.current_item.check_current_item()
    products_page.current_item.check_review_item()