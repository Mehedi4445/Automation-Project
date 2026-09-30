"""
Reusable multi-step flows that more than one test needs.
Keeping them here means a test only says WHAT it wants ("register a user"),
not every click needed to do it.
"""
from pages.login_page import LoginPage
from pages.account_page import AccountInformationPage, AccountCreatedPage
from utils.helpers import UserData


def register_user_from_login_page(page, user: UserData):
    """
    Starts on the 'Signup / Login' page. Fills the signup form and the full
    account information form, creates the account, checks 'ACCOUNT CREATED!'
    and clicks Continue. Used by: Login test (setup) and Download Invoice test.
    """
    LoginPage(page).start_signup(user.name, user.email)

    account_info_page = AccountInformationPage(page)
    account_info_page.fill_account_information(
        password=user.password, day=user.birth_day,
        month=user.birth_month, year=user.birth_year,
    )
    account_info_page.select_newsletter_and_offers()
    account_info_page.fill_address_information(
        first_name=user.first_name, last_name=user.last_name, company=user.company,
        address=user.address1, address2=user.address2, country=user.country,
        state=user.state, city=user.city, zipcode=user.zipcode,
        mobile_number=user.mobile_number,
    )
    account_info_page.click_create_account()

    account_created_page = AccountCreatedPage(page)
    assert account_created_page.get_confirmation_text() == "ACCOUNT CREATED!"
    account_created_page.click_continue()
