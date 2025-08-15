import pytest
from playwright.sync_api import Page

from fixtures.browsers import browser_page
from pages.api_cases_page.api_cases_page import ApiCasesPage
from pages.cart_page.cart_page import CartPage
from pages.contact_us.contact_us import ContactUsPage
from pages.login_page.login_page import LoginPage
from pages.products_page.products_page import ProductsPage
from pages.start_page.start_page import StartPage


@pytest.fixture
def start_page(browser_page: Page) -> StartPage:
    return StartPage(page=browser_page)


@pytest.fixture
def login_page(browser_page: Page) -> LoginPage:
    return LoginPage(page=browser_page)


@pytest.fixture
def cart_page(browser_page: Page) -> CartPage:
    return CartPage(page=browser_page)

@pytest.fixture
def products_page(browser_page: Page) -> ProductsPage:
    return ProductsPage(page=browser_page)
@pytest.fixture
def api_cases_page(browser_page: Page) -> ApiCasesPage:
    return ApiCasesPage(page=browser_page)

@pytest.fixture
def contact_us_page(browser_page:Page)-> ContactUsPage:
    return ContactUsPage(page=browser_page)