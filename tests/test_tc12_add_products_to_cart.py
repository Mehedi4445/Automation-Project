"""
Test Case 12: Add Products in Cart
Steps:
 1-3.  Launch browser, open the site, verify home page is visible
 4.    Click 'Products'
 5.    Hover over the first product and click 'Add to cart'
 6.    Click 'Continue Shopping'
 7.    Hover over the second product and click 'Add to cart'
 8.    Click 'View Cart'
 9.    Verify both products are added to the cart
 10.   Verify their prices, quantity and total price
"""
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.helpers import price_to_number


def test_add_products_to_cart(home_page):
    page = home_page.page

    # Step 3: home page is visible
    assert home_page.is_home_page_visible()

    # Step 4: click 'Products'
    home_page.go_to_products_page()
    products_page = ProductsPage(page)

    # Remember what the website shows for the first two products,
    # so we can compare it with the cart later.
    first_name, first_price = products_page.get_product_name(0), products_page.get_product_price(0)
    second_name, second_price = products_page.get_product_name(1), products_page.get_product_price(1)
    print(f"Adding: {first_name} ({first_price}) and {second_name} ({second_price})")

    # Steps 5-6: add the first product, then 'Continue Shopping'
    products_page.add_product_to_cart_by_index(0)
    products_page.close_add_to_cart_popup()

    # Step 7: add the second product
    products_page.add_product_to_cart_by_index(1)

    # Step 8: click 'View Cart'
    products_page.go_to_cart_from_popup()
    cart_page = CartPage(page)
    assert cart_page.is_cart_page_displayed()

    # Step 9: both products are in the cart
    assert cart_page.get_number_of_products_in_cart() == 2
    assert cart_page.is_product_in_cart(first_name)
    assert cart_page.is_product_in_cart(second_name)
    print("Both products are in the cart")

    # Step 10: price, quantity and total of each product
    items = {item["name"]: item for item in cart_page.get_cart_items()}
    for name, price in [(first_name, first_price), (second_name, second_price)]:
        item = items[name]
        assert item["price"] == price
        assert item["quantity"] == "1"
        assert price_to_number(item["total"]) == price_to_number(price) * 1
        print(f"{name}: price {item['price']}, quantity {item['quantity']}, total {item['total']}")
