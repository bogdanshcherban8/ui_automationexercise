import pytest
from playwright.sync_api import Page

from fixtures.browsers import browser_page
from pages.cart_page.cart_page import CartPage
from pages.login_page.login_page import LoginPage
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
