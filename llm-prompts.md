# LLM Prompts Log

Summary of prompts and iterative refinements used with AI assistance while building, debugging, and documenting the Nuaav QA Playwright assessment repository.

1. **Architecture & POM Scaffolding:** Requested a clean Python + pytest + Playwright Page Object Model layout (BasePage, LoginPage, InventoryPage, CartPage, CheckoutPage, conftest.py, and pytest.ini) targeting https://www.saucedemo.com with storageState session reuse.
2. **Test Coverage & Special Users:** Built test cases covering authentication, catalog sorting and item detail navigation, cart add/remove actions, three-step checkout totals (subtotal + tax == total), and SauceDemo special users (locked_out_user, problem_user, performance_glitch_user, error_user).
3. **Debugging & Stabilization:** Fixed page/context references (auth_inventory_page.page), scoped cart item locators (.cart_item), added cart cleanup for test isolation, and refined product detail and login assertions to avoid strict-mode or render timing issues.
4. **Documentation:** Generated README.md (including setup, HTML/parallel commands, design decisions, and a junior engineer onboarding guide) and this prompt log.
