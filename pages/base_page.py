from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page:Page):
        self.page=page
    def visit(self, url):
        with allure.step(f"Opening the url: {url}"):
            self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
    def check_current_url(self, expected_url:Pattern[str]):
        with allure.step(f"Checking that current url matches pattern {expected_url.pattern}"):
            expect(self.page).to_have_url(expected_url)