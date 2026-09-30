from playwright.sync_api import Page


class CheckoutPage:
    """Represents the 'Checkout' page (https://www.automationexercise.com/checkout)."""

    def __init__(self, page: Page):
        self.page = page
        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")
        self.order_review = page.locator("#cart_info")
        self.comment_box = page.locator("textarea[name='message']")
        self.place_order_button = page.locator("a[href='/payment']")

    def is_address_details_visible(self) -> bool:
        return self.delivery_address.is_visible() and self.billing_address.is_visible()

    def is_order_review_visible(self) -> bool:
        return self.order_review.is_visible()

    def get_delivery_address_text(self) -> str:
        return self.delivery_address.inner_text()

    def get_billing_address_text(self) -> str:
        return self.billing_address.inner_text()

    def is_product_in_order_review(self, product_name: str) -> bool:
        return self.order_review.locator("tbody tr").filter(has_text=product_name).count() > 0

    def enter_comment_and_place_order(self, comment: str):
        self.comment_box.fill(comment)
        self.place_order_button.click()
        self.page.wait_for_timeout(2000)
