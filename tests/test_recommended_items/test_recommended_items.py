import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.start_page.start_page import StartPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.RECOMMENDED_ITEMS)
@allure.epic(AllureEpic.UI)
@allure.story(AllureStory.RECOMMENDED_ITEMS)
@allure.severity(Severity.TRIVIAL)
@pytest.mark.recommended_items
@pytest.mark.smoke
@pytest.mark.no_path
@allure.title("Checking recommended items on static page")
def test_recommended_items_no_path(start_page:StartPage):
    start_page.visit(settings.app_url)
    start_page.recommended_items.check_recommended_items()
