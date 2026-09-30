"""
Test Case 1: Register User
Steps (from automationexercise.com/test_cases):
 1-3.  Launch browser, open the site, verify home page is visible   (home_page fixture)
 4.    Click 'Signup / Login'
 5.    Verify 'New User Signup!' is visible
 6-7.  Enter name and email, click 'Signup'
 8.    Verify 'ENTER ACCOUNT INFORMATION' is visible
 9.    Fill title, password, date of birth
 10-11 Tick 'Sign up for our newsletter!' and 'Receive special offers...'
 12.   Fill first/last name, company, address, address2, country, state, city, zipcode, mobile
 13.   Click 'Create Account'
 14.   Verify 'ACCOUNT CREATED!' is visible
 15.   Click 'Continue'
 16.   Verify 'Logged in as username' is visible
 17.   Click 'Delete Account'
 18.   Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
"""
from pages.login_page import LoginPage
from pages.account_page import AccountInformationPage, AccountCreatedPage, AccountDeletedPage


def test_register_user(home_page, new_user):
    page = home_page.page

    # Step 3: home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: 'New User Signup!' is visible
    login_page = LoginPage(page)
    assert login_page.is_signup_heading_visible()
    print("'New User Signup!' is visible")

    # Steps 6-7: enter name + email and click Signup
    login_page.start_signup(new_user.name, new_user.email)

    # Step 8: 'ENTER ACCOUNT INFORMATION' is visible
    account_info_page = AccountInformationPage(page)
    assert account_info_page.is_heading_visible()
    print("'ENTER ACCOUNT INFORMATION' is visible")

    # Steps 9-12: fill the whole form
    account_info_page.fill_account_information(
        password=new_user.password, day=new_user.birth_day,
        month=new_user.birth_month, year=new_user.birth_year,
    )
    account_info_page.select_newsletter_and_offers()
    assert account_info_page.newsletter_checkbox.is_checked()
    assert account_info_page.offers_checkbox.is_checked()
    account_info_page.fill_address_information(
        first_name=new_user.first_name, last_name=new_user.last_name,
        company=new_user.company, address=new_user.address1,
        address2=new_user.address2, country=new_user.country,
        state=new_user.state, city=new_user.city, zipcode=new_user.zipcode,
        mobile_number=new_user.mobile_number,
    )

    # Step 13: click 'Create Account'
    account_info_page.click_create_account()

    # Step 14: 'ACCOUNT CREATED!' is visible
    account_created_page = AccountCreatedPage(page)
    assert account_created_page.get_confirmation_text() == "ACCOUNT CREATED!"
    print("Account created successfully")

    # Step 15: click 'Continue'
    account_created_page.click_continue()

    # Step 16: 'Logged in as username' is visible
    assert home_page.is_logged_in_as(new_user.name)
    print(f"Logged in as {new_user.name}")

    # Step 17: click 'Delete Account'
    home_page.delete_account()

    # Step 18: 'ACCOUNT DELETED!' is visible, then click 'Continue'
    account_deleted_page = AccountDeletedPage(page)
    assert account_deleted_page.get_confirmation_text() == "ACCOUNT DELETED!"
    account_deleted_page.click_continue()
    print("Account deleted (cleanup done)")
