# Nuaav QA Playwright Assessment

Automated UI testing suite for [SauceDemo](https://www.saucedemo.com) built with **Python 3.12**, **pytest**, and **Playwright**, structured using the **Page Object Model (POM)** pattern.

> **Implementation Note:** Although the initial prompt referenced a TypeScript/Playwright example layout, implementing the solution in **Python + pytest + Playwright** was confirmed directly with Cristian during the assessment process.

## 1. Prerequisites & Setup

- **Python:** 3.12+
- **Browsers:** Chromium and Firefox (installed via Playwright)

``powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium firefox
