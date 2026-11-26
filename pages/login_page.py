from playwright.sync_api import Locator, Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")
        self.error_message: Locator = page.locator("[data-test='error']")
        self.error_close_button: Locator = page.locator("[data-test='error-button']")

    def open(self) -> None:
        self.navigate("/")

    def login(self, username: str, password: str = "secret_sauce") -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()
