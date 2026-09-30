"""
Test Case 24: Download Invoice after purchase order
Steps:
 1-3.  Launch browser, open the site, verify home page is visible
 4.    Add products to cart
 5.    Click 'Cart'
 6.    Verify the cart page is displayed
 7.    Click 'Proceed To Checkout'
 8.    Click 'Register / Login' (in the popup)
 9.    Fill all details in Signup and create account
 10.   Verify 'ACCOUNT CREATED!' and click 'Continue'
 11.   Verify 'Logged in as username' at top
 12.   Click 'Cart'
 13.   Click 'Proceed To Checkout'
 14.   Verify Address Details and Review Your Order
 15.   Enter a comment and click 'Place Order'
 16.   Enter payment details: name on card, card number, CVC, expiry
 17.   Click 'Pay and Confirm Order'
 18.   Verify the order was placed successfully
 19.   Click 'Download Invoice' and verify the invoice is downloaded
 20.   Click 'Continue'
 21.   Click 'Delete Account'
 22.   Verify 'ACCOUNT DELETED!' and click 'Continue'
"""
import os

from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlacedPage
from pages.account_page import AccountDeletedPage
from utils.flows import register_user_from_login_page


def test_download_invoice_after_purchase(home_page, new_user):
    page = home_page.page

    # Step 3: home page is visible
    assert home_page.is_home_page_visible()

    # Step 4: add a product to the cart
    home_page.go_to_products_page()
    products_page = ProductsPage(page)
    product_name = products_page.get_product_name(0)
    products_page.add_product_to_cart_by_index(0)
    products_page.close_add_to_cart_popup()

    # Steps 5-6: click 'Cart' and verify the cart page
    home_page.go_to_cart_page()
    cart_page = CartPage(page)
    assert cart_page.is_cart_page_displayed()
    assert cart_page.is_product_in_cart(product_name)

    # Steps 7-8: 'Proceed To Checkout', then 'Register / Login' in the popup
    cart_page.click_proceed_to_checkout()
    cart_page.click_register_login_in_popup()

    # Steps 9-10: sign up, create the account, 'ACCOUNT CREATED!', Continue
    register_user_from_login_page(page, new_user)
    print(f"Account created for {new_user.name}")

    # Step 11: 'Logged in as username' at top
    assert home_page.is_logged_in_as(new_user.name)

    # Steps 12-13: back to the cart, 'Proceed To Checkout' (no popup now, we are logged in)
    home_page.go_to_cart_page()
    cart_page.click_proceed_to_checkout()

    # Step 14: verify address details and review your order
    checkout_page = CheckoutPage(page)
    assert checkout_page.is_address_details_visible()
    assert checkout_page.is_order_review_visible()
    assert checkout_page.is_product_in_order_review(product_name)
    for address_text in (checkout_page.get_delivery_address_text(),
                         checkout_page.get_billing_address_text()):
        for expected in (new_user.first_name, new_user.last_name, new_user.address1,
                         new_user.city, new_user.country, new_user.mobile_number):
            assert expected in address_text
    print("Address details and order review are correct")

    # Step 15: enter a comment and click 'Place Order'
    checkout_page.enter_comment_and_place_order("Please deliver during office hours.")

    # Steps 16-17: payment details, then 'Pay and Confirm Order'
    payment_page = PaymentPage(page)
    payment_page.fill_payment_details(
        name="Test User", card_number="4111111111111111",
        cvc="123", expiry_month="12", expiry_year="2030",
    )
    payment_page.click_pay_and_confirm()

    # Step 18: order placed successfully
    order_placed_page = OrderPlacedPage(page)
    assert order_placed_page.get_heading_text().lower() == "order placed!"
    assert order_placed_page.is_confirmation_message_visible()
    print("Order placed successfully")

    # Step 19: 'Download Invoice' and verify the file was downloaded
    download = order_placed_page.download_invoice()
    downloaded_file = download.path()
    assert "invoice" in download.suggested_filename.lower()
    assert downloaded_file is not None and os.path.getsize(downloaded_file) > 0
    print(f"Invoice downloaded: {download.suggested_filename} ({os.path.getsize(downloaded_file)} bytes)")

    # Step 20: click 'Continue'
    order_placed_page.click_continue()

    # Steps 21-22: delete the account (cleanup) and verify
    home_page.delete_account()
    account_deleted_page = AccountDeletedPage(page)
    assert account_deleted_page.get_confirmation_text() == "ACCOUNT DELETED!"
    account_deleted_page.click_continue()
    print("Account deleted (cleanup done)")
