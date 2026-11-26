from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header_title: Locator = page.locator("[data-test='title']")
        self.cart_items: Locator = page.locator(".cart_item")
        self.item_names: Locator = page.locator(".cart_item [data-test='inventory-item-name']")
        self.continue_shopping_button: Locator = page.locator("[data-test='continue-shopping']")
        self.checkout_button: Locator = page.locator("[data-test='checkout']")

    def open(self) -> None:
        self.navigate("/cart.html")

    def get_cart_item_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def get_items_count(self) -> int:
        self.page.wait_for_url("**/cart.html")
        self.header_title.wait_for(state="visible")
        if self.cart_items.count() > 0:
            self.cart_items.first.wait_for(state="visible")
        return self.cart_items.count()

    def remove_item_by_slug(self, item_slug: str) -> None:
        self.page.locator(f"[data-test='remove-{item_slug}']").click()

    def continue_shopping(self) -> None:
        self.continue_shopping_button.click()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
