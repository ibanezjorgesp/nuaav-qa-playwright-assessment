from pathlib import Path
from typing import Generator
import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com"
AUTH_FILE = Path(".auth/standard_user.json")


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def auth_state_path(browser: Browser) -> str:
    """Authenticates once per test session as standard_user and saves storageState."""
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")

    context.storage_state(path=str(AUTH_FILE))
    context.close()
    return str(AUTH_FILE)


@pytest.fixture
def authenticated_context(
    browser: Browser, auth_state_path: str
) -> Generator[BrowserContext, None, None]:
    """Creates an isolated browser context preloaded with standard_user storageState."""
    context = browser.new_context(
        base_url=BASE_URL,
        storage_state=auth_state_path,
    )
    yield context
    context.close()


@pytest.fixture
def authenticated_page(
    authenticated_context: BrowserContext,
) -> Generator[Page, None, None]:
    page = authenticated_context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def auth_inventory_page(authenticated_page: Page) -> InventoryPage:
    inv = InventoryPage(authenticated_page)
    inv.open()
    inv.page.wait_for_url("**/inventory.html")
    return inv


@pytest.fixture
def auth_cart_page(authenticated_page: Page) -> CartPage:
    return CartPage(authenticated_page)


@pytest.fixture
def auth_checkout_page(authenticated_page: Page) -> CheckoutPage:
    return CheckoutPage(authenticated_page)
