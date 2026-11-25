import pytest
from playwright.sync_api import Page

@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://example.com")
    return page
