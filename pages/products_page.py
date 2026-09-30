from playwright.sync_api import Page


class ProductsPage:
    """Represents the 'All Products' page (https://www.automationexercise.com/products)."""

    def __init__(self, page: Page):
        self.page = page

        self.all_products_title = page.locator("h2.title")
        self.product_items = page.locator(".features_items .product-image-wrapper")

        # Popup that appears right after clicking "Add to cart"
        # NOTE: "a[href='/view_cart']" also matches the navbar's Cart icon,
        # so we scope this locator to just the popup itself (#cartModal).
        self.continue_shopping_button = page.locator("button:has-text('Continue Shopping')")
        self.view_cart_link_in_popup = page.locator("#cartModal a[href='/view_cart']")

    def get_number_of_products(self) -> int:
        return self.product_items.count()

    def get_product_name(self, index: int) -> str:
        """Name shown on the product card (first = 0)."""
        return self.product_items.nth(index).locator(".productinfo p").inner_text().strip()

    def get_product_price(self, index: int) -> str:
        """Price text shown on the product card, e.g. 'Rs. 500'."""
        return self.product_items.nth(index).locator(".productinfo h2").inner_text().strip()

    def add_product_to_cart_by_index(self, index: int = 0):
        """
        Hovers over a product card (by position, first = 0) and clicks
        its 'Add to cart' button. A popup then appears.
        """
        product_card = self.product_items.nth(index)
        product_card.hover()
        product_card.locator("a:has-text('Add to cart')").first.click()
        self.page.wait_for_timeout(1500)

    def close_add_to_cart_popup(self):
        """Clicks 'Continue Shopping' in the popup."""
        self.continue_shopping_button.click()
        self.page.wait_for_timeout(1000)

    def go_to_cart_from_popup(self):
        """Clicks 'View Cart' in the popup."""
        self.view_cart_link_in_popup.click()
        self.page.wait_for_timeout(2000)
