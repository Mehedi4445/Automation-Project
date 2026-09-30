"""
Test Case 13: Verify Product quantity in Cart
Steps:
 1-3.  Launch browser, open the site, verify home page is visible
 4.    Click 'View Product' for a product on the home page
 5.    Verify the product detail page is opened
 6.    Increase quantity to 4
 7.    Click 'Add to cart'
 8.    Click 'View Cart'
 9.    Verify the product is in the cart with the exact quantity
"""
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from utils.helpers import price_to_number

QUANTITY = 4


def test_verify_product_quantity_in_cart(home_page):
    page = home_page.page

    # Step 3: home page is visible
    assert home_page.is_home_page_visible()

    # Step 4: click 'View Product' on the first product
    home_page.click_view_product_by_index(0)

    # Step 5: product detail page is opened
    detail_page = ProductDetailPage(page)
    assert "/product_details/" in page.url
    assert detail_page.is_product_detail_visible()
    product_name = detail_page.get_product_name()
    product_price = detail_page.get_product_price()
    print(f"Product detail page opened: {product_name} ({product_price})")

    # Step 6: increase quantity to 4
    detail_page.set_quantity(QUANTITY)

    # Step 7: click 'Add to cart'
    detail_page.click_add_to_cart()

    # Step 8: click 'View Cart'
    detail_page.go_to_cart_from_popup()

    # Step 9: product is in the cart with the exact quantity
    cart_page = CartPage(page)
    assert cart_page.is_cart_page_displayed()
    assert cart_page.get_number_of_products_in_cart() == 1

    item = cart_page.get_cart_items()[0]
    assert item["name"] == product_name
    assert item["quantity"] == str(QUANTITY)
    assert price_to_number(item["total"]) == price_to_number(product_price) * QUANTITY
    print(f"Cart shows {item['name']} x {item['quantity']} = {item['total']}")
