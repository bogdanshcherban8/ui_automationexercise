

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.start_page.start_page import StartPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.CAROUSEL)
@allure.epic(AllureEpic.UI)
@allure.story(AllureStory.CAROUSEL)
@pytest.mark.carousel
@pytest.mark.smoke
@pytest.mark.no_path
@allure.severity(Severity.TRIVIAL)
@allure.title("Checking carousel on static pages")
@pytest.mark.flacky(rerun=3, delay=2)
def test_carousel_no_path(start_page: StartPage):
    start_page.visit(settings.app_url)
    start_page.carousel.check_carousel()