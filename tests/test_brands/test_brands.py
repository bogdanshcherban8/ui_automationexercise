from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.start_page.start_page import StartPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.BRANDS)
@allure.epic(AllureEpic.UI)
@pytest.mark.brands
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking brands on static pages")
@allure.severity(Severity.MINOR)
@allure.story(AllureStory.BRANDS)
@pytest.mark.flacky(reruns=3, reruns_delay=2)
@pytest.mark.parametrize("url", [settings.app_url, urljoin(settings.app_url, "products"), urljoin(settings.app_url, "product_details/1")])
def test_brands_no_path(start_page:StartPage, url):
    start_page.visit(url)
    start_page.brands.check_brands_title()
    start_page.brands.check_brands()