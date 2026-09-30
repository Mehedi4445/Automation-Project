# AutomationExercise v2 - Playwright + Pytest (Page Object Model)

Automated tests for https://www.automationexercise.com/ covering these six
test cases from the site's Test Cases page:

| TC  | Scenario                                    | File                                          |
|-----|---------------------------------------------|-----------------------------------------------|
| 1   | Register User                               | `tests/test_tc01_register_user.py`            |
| 2   | Login User with correct email and password  | `tests/test_tc02_login_correct_credentials.py`|
| 3   | Login User with incorrect email and password| `tests/test_tc03_login_incorrect_credentials.py` |
| 12  | Add Products in Cart                        | `tests/test_tc12_add_products_to_cart.py`     |
| 13  | Verify Product quantity in Cart             | `tests/test_tc13_verify_product_quantity.py`  |
| 24  | Download Invoice after purchase order       | `tests/test_tc24_download_invoice.py`         |

Each test has the site's numbered steps written as comments, so you can
match every line of code to a step.

## Project Structure

```
AutomationExercise_v2/
├── conftest.py                 # fixtures: page, home_page, new_user, registered_user
├── pytest.ini
├── requirements.txt
├── pages/                      # Page Object Model - one file per page
│   ├── home_page.py            # navbar, home products, logout / delete account
│   ├── login_page.py           # login(), start_signup(), heading checks
│   ├── account_page.py         # account info form / created / deleted pages
│   ├── products_page.py        # product cards, add to cart, cart popup
│   ├── product_detail_page.py  # product details, quantity, add to cart
│   ├── cart_page.py            # cart rows, checkout button, Register/Login popup
│   ├── checkout_page.py        # addresses, order review, comment, place order
│   ├── payment_page.py         # card details, pay button
│   └── order_placed_page.py    # order confirmation, download invoice
├── utils/
│   ├── helpers.py              # unique email/name, UserData, price_to_number()
│   └── flows.py                # register_user_from_login_page() - shared signup flow
└── tests/                      # one test case per file
```

## What changed compared with the first project

- Kept only the six test cases above. Contact Us, Search Product and Verify
  Test Cases Page (and their page objects) were removed.
- Test Case 1 now follows all 18 steps: newsletter and offers checkboxes,
  company and address2 fields, and the 'New User Signup!' / 'ENTER ACCOUNT
  INFORMATION' checks. Account deletion moved into `HomePage.delete_account()`.
- Every test now verifies that the home page is visible (step 3).
- Test Case 12 adds the first and second product and checks name, price,
  quantity and total in the cart (before it added one product and counted rows).
- New page objects: product detail, checkout, payment, order placed.
- New fixtures: `new_user` (unique user data) and `registered_user` (creates a
  real account, then logs out) used by Test Case 2.
- The shared signup steps live in one function, `register_user_from_login_page()`.
- `requirements.txt` no longer pins exact versions (`pytest>=8.3.3`,
  `playwright>=1.47.0`), so it works with newer Python and pytest versions.
- The browser is visible by default; set `HEADLESS=1` to run without a window.

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

## Run

Run all commands from inside the `AutomationExercise_v2` folder.

```bash
pytest                                              # all six tests
pytest tests/test_tc24_download_invoice.py          # a single test
HEADLESS=1 pytest                                   # no browser window (Windows PowerShell: $env:HEADLESS=1; pytest)
```

## Notes

- Every test that creates an account uses a fresh random email
  (`utils/helpers.py`), so tests can be re-run without 'Email Address already
  exist!' errors. TC 1, 2 and 24 delete their account at the end. If a test
  fails halfway, that one account is left on the website, which is harmless.
- TC 24: the site's steps mention the message 'Your order has been placed
  successfully!'. The test checks the 'ORDER PLACED!' heading and the
  'Your order has been confirmed' text on the page that follows payment.
  The invoice check confirms a file named like `invoice...` was downloaded and
  is not empty.
- If a locator ever stops working, open the page in your browser, right-click
  the element -> Inspect, and update the matching line in `pages/`.
