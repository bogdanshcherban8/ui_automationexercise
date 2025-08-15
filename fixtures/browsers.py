import hashlib
import re

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from config import settings
from tools.mocks import mock_static_resources


def sanitize_filename(name: str) -> str:

    safe_name = re.sub(r'[<>:"/\\|?*]', '_', name)

    if len(safe_name) > 50:
        hash_suffix = hashlib.md5(name.encode()).hexdigest()
        safe_name = safe_name[:30] + "_" + hash_suffix
    return safe_name
@pytest.fixture(params=settings.browsers)
def browser_page(playwright:Playwright, request:SubRequest)->Page:
    browser_type=request.param
    browser=playwright[browser_type].launch(headless=settings.headless)
    context=browser.new_context(record_video_dir=settings.record_video_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)
    yield page
    path = f"{settings.tracing_path}/{sanitize_filename(request.node.name)}.zip"
    context.tracing.stop(path=path)
    browser.close()
    allure.attach.file(path, name="trace", extension='zip')
    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)