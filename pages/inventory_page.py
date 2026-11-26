from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header_title: Locator = page.locator("[data-test='title']")
        self.inventory_container: Locator = page.locator("[data-test='inventory-container']")
        self.inventory_items: Locator = page.locator(".inventory_item")
        self.item_names: Locator = page.locator("[data-test='inventory-item-name']")
        self.item_prices: Locator = page.locator("[data-test='inventory-item-price']")
        self.item_images: Locator = page.locator(".inventory_item img")
        self.sort_dropdown: Locator = page.locator("[data-test='product-sort-container']")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link: Locator = page.locator("[data-test='shopping-cart-link']")
        self.burger_menu_button: Locator = page.locator("#react-burger-menu-btn")
        self.logout_link: Locator = page.locator("[data-test='logout-sidebar-link']")
        self.reset_app_link: Locator = page.locator("[data-test='reset-sidebar-link']")

    def open(self) -> None:
        self.navigate("/inventory.html")

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible() and self.header_title.inner_text() == "Products"

    def sort_by(self, option_value: str) -> None:
        """Valid options: 'az', 'za', 'lohi', 'hilo'."""
        self.sort_dropdown.select_option(option_value)

    def get_all_item_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def get_all_item_prices(self) -> list[float]:
        raw_prices = self.item_prices.all_inner_texts()
        return [float(price.replace("$", "").strip()) for price in raw_prices]

    def get_all_image_sources(self) -> list[str]:
        self.item_images.first.wait_for(state="visible")
        return [
            img.get_attribute("src") or ""
            for img in self.item_images.all()
        ]

    def add_item_to_cart_by_slug(self, item_slug: str) -> None:
        """Example slug: 'sauce-labs-backpack'."""
        self.page.locator(f"[data-test='add-to-cart-{item_slug}']").click()

    def remove_item_from_cart_by_slug(self, item_slug: str) -> None:
        self.page.locator(f"[data-test='remove-{item_slug}']").click()

    def clear_cart_if_needed(self) -> None:
        for remove_btn in self.page.locator("[data-test^='remove-']").all():
            if remove_btn.is_visible():
                remove_btn.click()

    def open_item_detail(self, item_name: str) -> None:
        self.item_names.filter(has_text=item_name).first.click()

    def get_cart_count(self) -> int:
        if not self.cart_badge.is_visible():
            return 0
        return int(self.cart_badge.inner_text())

    def go_to_cart(self) -> None:
        self.cart_link.click()

    def logout(self) -> None:
        self.burger_menu_button.click()
        self.logout_link.click()
