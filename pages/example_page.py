from pages.base_page import BasePage

class ExamplePage(BasePage):
    def open_home(self):
        self.navigate("https://example.com")
