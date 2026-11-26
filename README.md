# Nuaav QA Playwright Assessment

Automated UI testing suite for [SauceDemo](https://www.saucedemo.com) built with **Python 3.12**, **pytest**, and **Playwright**, structured using the **Page Object Model (POM)** pattern.

> **Implementation Note:** Although the initial prompt referenced a TypeScript/Playwright example layout, implementing the solution in **Python + pytest + Playwright** was confirmed directly with Cristian during the assessment process.

## Project Structure

- `pages/`: Page objects (`BasePage`, `LoginPage`, `InventoryPage`, `CartPage`, `CheckoutPage`) encapsulating locators and UI interactions.
- `tests/`: Test modules covering authentication (`test_auth.py`), inventory and cart (`test_inventory_and_cart.py`), and checkout (`test_checkout.py`), including SauceDemo behavioral users (`locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`).
- `conftest.py`: Session-scoped authentication via `storageState` (`.auth/standard_user.json`), isolated browser context/page fixtures, and automatic CI retry configuration (`retries = 1` when `CI` is set).
- `pytest.ini`: Configures `base_url`, multi-browser execution (`chromium` and `firefox`), test discovery, and failure screenshots under `test-results/`.

## Setup

``powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium firefox
