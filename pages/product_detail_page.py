from playwright.sync_api import Page


class ProductDetailPage:
    """Represents one product's detail page (https://www.automationexercise.com/product_details/<id>)."""

    def __init__(self, page: Page):
        self.page = page

        info = page.locator(".product-information")
        self.product_information = info
        self.name = info.locator("h2")
        self.category = info.locator("p:has-text('Category')")
        self.price = info.locator("span span").first
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.locator("button.cart")

        # Popup after clicking "Add to cart" (scoped to #cartModal, see ProductsPage)
        self.view_cart_link_in_popup = page.locator("#cartModal a[href='/view_cart']")

    def is_product_detail_visible(self) -> bool:
        return self.product_information.is_visible()

    def get_product_name(self) -> str:
        return self.name.inner_text().strip()

    def get_product_price(self) -> str:
        return self.price.inner_text().strip()

    def set_quantity(self, quantity: int):
        """Replaces the quantity (default 1) with the number we want."""
        self.quantity_input.fill(str(quantity))

    def click_add_to_cart(self):
        self.add_to_cart_button.click()
        self.page.wait_for_timeout(1500)

    def go_to_cart_from_popup(self):
        self.view_cart_link_in_popup.click()
        self.page.wait_for_timeout(2000)
