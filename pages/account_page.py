from playwright.sync_api import Page


class AccountInformationPage:
    """
    Represents the 'Enter Account Information' page that appears
    after submitting the small signup form (name + email).
    """

    def __init__(self, page: Page):
        self.page = page

        self.heading = page.locator("h2:has-text('Enter Account Information')")

        self.title_mr = page.locator("#id_gender1")
        self.password = page.locator("#password")
        self.days = page.locator("#days")
        self.months = page.locator("#months")
        self.years = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")

        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company = page.locator("#company")
        self.address1 = page.locator("#address1")
        self.address2 = page.locator("#address2")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile_number = page.locator("#mobile_number")

        self.create_account_button = page.locator('button[data-qa="create-account"]')

    def is_heading_visible(self) -> bool:
        return self.heading.is_visible()

    def fill_account_information(self, password: str, day: str, month: str, year: str):
        """Fills the top part of the form: title, password and date of birth."""
        self.title_mr.check()
        self.password.fill(password)
        self.days.select_option(day)
        self.months.select_option(month)
        self.years.select_option(year)
        self.page.wait_for_timeout(500)

    def select_newsletter_and_offers(self):
        """Ticks both checkboxes: newsletter + special offers from partners."""
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()

    def fill_address_information(self, first_name: str, last_name: str, company: str,
                                 address: str, address2: str, country: str,
                                 state: str, city: str, zipcode: str,
                                 mobile_number: str):
        """Fills the bottom part of the form: name and address details."""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address1.fill(address)
        self.address2.fill(address2)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)
        self.page.wait_for_timeout(500)

    def click_create_account(self):
        self.create_account_button.click()
        self.page.wait_for_timeout(2000)


class AccountCreatedPage:
    """Represents the small 'ACCOUNT CREATED!' confirmation page."""

    def __init__(self, page: Page):
        self.page = page
        self.account_created_text = page.locator('h2[data-qa="account-created"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def get_confirmation_text(self) -> str:
        return self.account_created_text.inner_text().strip()

    def click_continue(self):
        self.continue_button.click()
        self.page.wait_for_timeout(2000)


class AccountDeletedPage:
    """Represents the small 'ACCOUNT DELETED!' confirmation page."""

    def __init__(self, page: Page):
        self.page = page
        self.account_deleted_text = page.locator('h2[data-qa="account-deleted"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def get_confirmation_text(self) -> str:
        return self.account_deleted_text.inner_text().strip()

    def click_continue(self):
        self.continue_button.click()
        self.page.wait_for_timeout(2000)
