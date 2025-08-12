

import allure
import pytest

from config import settings
from pages.start_page.start_page import StartPage

@pytest.mark.carousel
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking carousel on static pages")
def test_carousel_no_path(start_page: StartPage):
    start_page.visit(settings.app_url)
    start_page.carousel.check_carousel()