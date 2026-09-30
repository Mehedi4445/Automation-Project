import re

from playwright.sync_api import Page, Download


class OrderPlacedPage:
    """Represents the 'ORDER PLACED!' page shown after paying (…/payment_done/<amount>)."""

    def __init__(self, page: Page):
        self.page = page
        self.order_placed_heading = page.locator('h2[data-qa="order-placed"]')
        self.confirmation_message = page.get_by_text(
            re.compile("your order has been confirmed", re.IGNORECASE)
        )
        self.download_invoice_button = page.locator("a:has-text('Download Invoice')")
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def get_heading_text(self) -> str:
        return self.order_placed_heading.inner_text().strip()

    def is_confirmation_message_visible(self) -> bool:
        return self.confirmation_message.first.is_visible()

    def download_invoice(self) -> Download:
        """
        Clicks 'Download Invoice' and waits for the browser to start the
        download. Returns the Download object so the test can inspect the file.
        """
        with self.page.expect_download() as download_info:
            self.download_invoice_button.click()
        return download_info.value

    def click_continue(self):
        self.continue_button.click()
        self.page.wait_for_timeout(2000)
