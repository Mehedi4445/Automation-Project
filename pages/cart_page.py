from playwright.sync_api import Page


class CartPage:
    """Represents the 'Cart' page (https://www.automationexercise.com/view_cart)."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_info = page.locator("#cart_info")
        self.cart_rows = page.locator("#cart_info tbody tr")
        self.proceed_to_checkout_button = page.locator("a.check_out")

        # Popup shown when a NOT logged-in user clicks 'Proceed To Checkout'
        self.register_login_link_in_popup = page.locator("#checkoutModal a[href='/login']")

    def is_cart_page_displayed(self) -> bool:
        return "/view_cart" in self.page.url and self.cart_info.is_visible()

    def get_number_of_products_in_cart(self) -> int:
        return self.cart_rows.count()

    def is_product_in_cart(self, product_name: str) -> bool:
        return self.cart_rows.filter(has_text=product_name).count() > 0

    def get_cart_items(self) -> list:
        """
        Reads every row of the cart table and returns a list like:
        [{"name": "Blue Top", "price": "Rs. 500", "quantity": "1", "total": "Rs. 500"}, ...]
        """
        items = []
        for i in range(self.cart_rows.count()):
            row = self.cart_rows.nth(i)
            items.append({
                "name": row.locator(".cart_description h4 a").inner_text().strip(),
                "price": row.locator(".cart_price p").inner_text().strip(),
                "quantity": row.locator(".cart_quantity button").inner_text().strip(),
                "total": row.locator(".cart_total_price").inner_text().strip(),
            })
        return items

    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()
        self.page.wait_for_timeout(2000)

    def click_register_login_in_popup(self):
        self.register_login_link_in_popup.click()
        self.page.wait_for_timeout(2000)
