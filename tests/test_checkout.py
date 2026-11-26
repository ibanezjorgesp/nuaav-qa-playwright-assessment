from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_checkout_missing_first_name_shows_error(
    auth_inventory_page: InventoryPage,
    auth_cart_page: CartPage,
    auth_checkout_page: CheckoutPage,
) -> None:
    auth_inventory_page.clear_cart_if_needed()
    auth_inventory_page.add_item_to_cart_by_slug("sauce-labs-bike-light")
    auth_inventory_page.go_to_cart()
    auth_cart_page.proceed_to_checkout()

    auth_checkout_page.fill_customer_info("", "Ibanez", "110111")
    auth_checkout_page.continue_checkout()

    assert "First Name is required" in auth_checkout_page.get_error_text()


def test_complete_three_step_checkout_flow(
    auth_inventory_page: InventoryPage,
    auth_cart_page: CartPage,
    auth_checkout_page: CheckoutPage,
) -> None:
    auth_inventory_page.clear_cart_if_needed()
    auth_inventory_page.add_item_to_cart_by_slug("sauce-labs-backpack")
    auth_inventory_page.add_item_to_cart_by_slug("sauce-labs-bolt-t-shirt")
    assert auth_inventory_page.get_cart_count() == 2

    auth_inventory_page.go_to_cart()
    assert auth_cart_page.get_items_count() == 2
    auth_cart_page.proceed_to_checkout()

    auth_checkout_page.fill_customer_info("Jorge", "Ibanez", "110111")
    auth_checkout_page.continue_checkout()
    expect(auth_checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    subtotal = auth_checkout_page.get_subtotal()
    tax = auth_checkout_page.get_tax()
    total = auth_checkout_page.get_total()
    assert round(subtotal + tax, 2) == round(total, 2)

    auth_checkout_page.finish_order()
    expect(auth_checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    assert auth_checkout_page.get_confirmation_header() == "Thank you for your order!"


def test_error_user_checkout_behavior(login_page: LoginPage, page: Page) -> None:
    login_page.open()
    login_page.login("error_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart_by_slug("sauce-labs-backpack")
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_customer_info("Jorge", "Ibanez", "110111")
    checkout.continue_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout.subtotal_label).to_be_visible()
