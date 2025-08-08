import pytest
from playwright.sync_api import Playwright, Page

from config import settings


@pytest.fixture(params=settings.browsers)
def browser_page(playwright:Playwright, request)->Page:
    browser_type=request.param
    browser=playwright[browser_type].launch(headless=settings.headless)
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
    browser.close()