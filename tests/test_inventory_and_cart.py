import time
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_sort_products_by_price_low_to_high(auth_inventory_page: InventoryPage) -> None:
    auth_inventory_page.sort_by("lohi")
    prices = auth_inventory_page.get_all_item_prices()
    assert prices == sorted(prices)


def test_sort_products_by_name_z_to_a(auth_inventory_page: InventoryPage) -> None:
    auth_inventory_page.sort_by("za")
    names = auth_inventory_page.get_all_item_names()
    assert names == sorted(names, reverse=True)


def test_open_product_detail_page(auth_inventory_page: InventoryPage) -> None:
    target_item = "Sauce Labs Backpack"
    auth_inventory_page.open_item_detail(target_item)

    expect(auth_inventory_page.page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    expect(auth_inventory_page.page.locator(".inventory_details_name")).to_have_text(target_item)


def test_add_and_remove_items_in_cart(
    auth_inventory_page: InventoryPage,
    auth_cart_page: CartPage,
) -> None:
    auth_inventory_page.clear_cart_if_needed()
    slug = "sauce-labs-backpack"
    auth_inventory_page.add_item_to_cart_by_slug(slug)
    assert auth_inventory_page.get_cart_count() == 1

    auth_inventory_page.go_to_cart()
    assert "Sauce Labs Backpack" in auth_cart_page.get_cart_item_names()
    assert auth_cart_page.get_items_count() == 1

    auth_cart_page.remove_item_by_slug(slug)
    assert auth_cart_page.get_items_count() == 0


def test_problem_user_catalog_images(login_page: LoginPage, page: Page) -> None:
    login_page.open()
    login_page.login("problem_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory = InventoryPage(page)
    sources = inventory.get_all_image_sources()
    assert len(sources) > 0
    assert len(set(sources)) < len(sources)


def test_performance_glitch_user_inventory_load_time(
    login_page: LoginPage,
    page: Page,
) -> None:
    max_allowed_seconds = 10.0

    login_page.open()
    start_time = time.perf_counter()
    login_page.login("performance_glitch_user", "secret_sauce")

    inventory = InventoryPage(page)
    expect(inventory.inventory_container).to_be_visible(timeout=int(max_allowed_seconds * 1000))
    elapsed_seconds = time.perf_counter() - start_time

    assert elapsed_seconds <= max_allowed_seconds, (
        f"Inventory loaded in {elapsed_seconds:.2f}s, exceeding {max_allowed_seconds:.2f}s"
    )
