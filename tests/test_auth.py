import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_success_standard_user(login_page: LoginPage, page: Page) -> None:
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory = InventoryPage(page)
    expect(inventory.inventory_container).to_be_visible()
    expect(inventory.header_title).to_have_text("Products")


def test_login_locked_out_user(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_visible()
    assert "locked out" in login_page.get_error_text().lower()


@pytest.mark.parametrize(
    ("username", "password", "expected_fragment"),
    [
        ("standard_user", "wrong_password", "username and password do not match"),
        ("invalid_user", "secret_sauce", "username and password do not match"),
        ("", "secret_sauce", "username is required"),
        ("standard_user", "", "password is required"),
    ],
)
def test_login_invalid_credentials(
    login_page: LoginPage,
    username: str,
    password: str,
    expected_fragment: str,
) -> None:
    login_page.open()
    login_page.login(username, password)

    assert login_page.is_error_visible()
    assert expected_fragment in login_page.get_error_text().lower()


def test_logout_from_inventory(auth_inventory_page: InventoryPage) -> None:
    assert auth_inventory_page.is_loaded()
    auth_inventory_page.logout()

    expect(auth_inventory_page.page).to_have_url("https://www.saucedemo.com/")
    expect(auth_inventory_page.page.locator("[data-test='login-button']")).to_be_visible()
