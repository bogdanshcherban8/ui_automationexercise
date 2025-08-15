from urllib.parse import urljoin

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.contact_us.contact_us import ContactUsPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.feature(AllureFeature.CONTACT_US)
@allure.epic(AllureEpic.UI)
@allure.story(AllureStory.CONTACT_US)
@pytest.mark.smoke
@pytest.mark.contact_us
@pytest.mark.no_path
@allure.title("Checking contact us page")
@allure.severity(Severity.MINOR)
def test_contact_us(contact_us_page:ContactUsPage):
    contact_us_page.visit(urljoin(settings.app_url, "contact_us"))
    contact_us_page.contact_us.check_contact_us()