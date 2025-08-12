from urllib.parse import urljoin

import allure
import pytest

from config import settings
from pages.products_page.products_page import ProductsPage


@pytest.mark.search_product
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking search products on static page")
def test_search_products_no_path(products_page:ProductsPage):
    products_page.visit(urljoin(settings.app_url, "products"))
    products_page.search_product.check_container()
    products_page.items.check_item()
    products_page.search_product.check_search_product()
    products_page.items.check_item()
    products_page.items.added_item()