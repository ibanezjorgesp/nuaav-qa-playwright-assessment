Markdown

\# Nuaav QA Playwright Assessment



Automated UI testing suite for \[SauceDemo](https://www.saucedemo.com) built with \*\*Python 3.12\*\*, \*\*pytest\*\*, and \*\*Playwright\*\*, structured using the \*\*Page Object Model (POM)\*\* pattern.



> \*\*Implementation Note:\*\* Although the initial prompt referenced a TypeScript/Playwright example layout, implementing the solution in \*\*Python + pytest + Playwright\*\* was confirmed directly with Cristian during the assessment process.



\## 1. Prerequisites



\- \*\*Python:\*\* 3.12+

\- \*\*Browsers:\*\* Chromium and Firefox (installed via Playwright)



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

playwright install chromium Firefox





2\. Running All Tests and Expected Output

Run the full test suite across both configured browsers (Chromium and Firefox) from the repository root:



PowerShell

pytest -v

Expected output:



Plaintext

collected 32 items

...

================================ 32 passed in \~70.00s ================================

(16 functional test scenarios executed across 2 browsers = 32 passed checks).





3\. Running a Specific Test File or Test by Name

PowerShell

\# Run a single test file

pytest -v tests/test\_auth.py



\# Run a specific test by name (substring match)

pytest -v -k "test\_complete\_three\_step\_checkout\_flow"



\# Run on a single browser only

pytest -v --browser chromium





4\. Generating and Viewing the HTML Report

Generate a self-contained HTML report using pytest-html (included in requirements.txt):



PowerShell

pytest -v --html=report.html --self-contained-html

To view it after a run, open report.html directly in any web browser, or launch it from PowerShell:



PowerShell

start report.html





5\. Key Design Decisions and Trade-offs

The suite uses a strict Page Object Model (POM) under pages/ (BasePage, LoginPage, InventoryPage, CartPage, CheckoutPage) so locators and UI interactions stay decoupled from test assertions in tests/. For test isolation, conftest.py authenticates standard\_user once per session into .auth/standard\_user.json via storageState and spawns fresh browser contexts per test, while cart tests explicitly clear leftover items before running. Default Playwright timeouts (30s actions, 5s expect) are preserved for SauceDemo's lightweight SPA, paired with an explicit 10.0s threshold for performance\_glitch\_user and automatic reruns = 1 when CI is set. Given the time constraint, the main trade-off was focusing on deterministic E2E functional coverage and SauceDemo's special user behaviors (locked\_out\_user, problem\_user, performance\_glitch\_user, error\_user) rather than adding visual regression snapshots or a remote GitHub Actions pipeline.



Onboarding a Junior Engineer

Welcome to the Playwright + pytest automation suite for SauceDemo. Start by creating a virtual environment with Python 3.12, activating it, installing dependencies from requirements.txt, and running playwright install chromium firefox so the required browser binaries are available locally. Once setup is complete, run pytest -v to verify that all 32 checks pass against https://www.saucedemo.com on both Chromium and Firefox.



As you explore the codebase, follow the separation of responsibilities between pages/ and tests/. Each page object in pages/ inherits from BasePage and exposes focused actions and locators for a single area of the application, such as login, catalog sorting and cart badges, cart item management, or the three-step checkout flow. Keep selectors and low-level browser waits inside the page objects rather than scattering raw locators across test functions.



Pay special attention to test isolation and authentication setup in conftest.py. A session-level fixture logs in once as standard\_user and saves storageState to .auth/standard\_user.json, while per-test fixtures create fresh browser contexts from that state. Whenever a test modifies cart state, clear any leftover items first so tests do not interfere with one another during sequential or parallel runs (pytest -n auto).



When adding a new test case, first check whether an existing page object already provides the needed action or add a focused helper method there. Use Playwright expect(...) assertions with built-in auto-waiting instead of manual sleep calls, inspect screenshots under test-results/ if anything fails, and run the suite on both Chromium and Firefox before opening a pull request.


