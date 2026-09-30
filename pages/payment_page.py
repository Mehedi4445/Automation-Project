from playwright.sync_api import Page


class PaymentPage:
    """Represents the 'Payment' page (https://www.automationexercise.com/payment)."""

    def __init__(self, page: Page):
        self.page = page
        self.name_on_card = page.locator('input[data-qa="name-on-card"]')
        self.card_number = page.locator('input[data-qa="card-number"]')
        self.cvc = page.locator('input[data-qa="cvc"]')
        self.expiry_month = page.locator('input[data-qa="expiry-month"]')
        self.expiry_year = page.locator('input[data-qa="expiry-year"]')
        self.pay_button = page.locator('button[data-qa="pay-button"]')

    def fill_payment_details(self, name: str, card_number: str, cvc: str,
                             expiry_month: str, expiry_year: str):
        """Fills the whole card form. One function, five fields."""
        self.name_on_card.fill(name)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)

    def click_pay_and_confirm(self):
        self.pay_button.click()
        self.page.wait_for_timeout(2000)
