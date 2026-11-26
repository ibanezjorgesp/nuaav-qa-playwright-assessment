from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Step One: Your Information
        self.header_title: Locator = page.locator("[data-test='title']")
        self.first_name_input: Locator = page.locator("[data-test='firstName']")
        self.last_name_input: Locator = page.locator("[data-test='lastName']")
        self.postal_code_input: Locator = page.locator("[data-test='postalCode']")
        self.continue_button: Locator = page.locator("[data-test='continue']")
        self.cancel_button: Locator = page.locator("[data-test='cancel']")
        self.error_message: Locator = page.locator("[data-test='error']")

        # Step Two: Overview
        self.summary_items: Locator = page.locator("[data-test='inventory-item']")
        self.subtotal_label: Locator = page.locator("[data-test='subtotal-label']")
        self.tax_label: Locator = page.locator("[data-test='tax-label']")
        self.total_label: Locator = page.locator("[data-test='total-label']")
        self.finish_button: Locator = page.locator("[data-test='finish']")

        # Step Three: Complete
        self.complete_header: Locator = page.locator("[data-test='complete-header']")
        self.complete_text: Locator = page.locator("[data-test='complete-text']")
        self.back_home_button: Locator = page.locator("[data-test='back-to-products']")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self) -> None:
        self.continue_button.click()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()

    def get_subtotal(self) -> float:
        text = self.subtotal_label.inner_text()
        return float(text.split("$")[-1].strip())

    def get_tax(self) -> float:
        text = self.tax_label.inner_text()
        return float(text.split("$")[-1].strip())

    def get_total(self) -> float:
        text = self.total_label.inner_text()
        return float(text.split("$")[-1].strip())

    def finish_order(self) -> None:
        self.finish_button.click()

    def get_confirmation_header(self) -> str:
        return self.complete_header.inner_text()
