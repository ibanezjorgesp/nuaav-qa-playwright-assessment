from pages.example_page import ExamplePage

def test_example_domain_loads(page):
    example_page = ExamplePage(page)
    example_page.open_home()
    assert "Example Domain" in example_page.get_title()
