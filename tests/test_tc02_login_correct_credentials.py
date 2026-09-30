"""
Test Case 2: Login User with correct email and password
Steps:
 1-3.  Launch browser, open the site, verify home page is visible
 4.    Click 'Signup / Login'
 5.    Verify 'Login to your account' is visible
 6-7.  Enter correct email and password, click 'Login'
 8.    Verify 'Logged in as username' is visible
 9.    Click 'Delete Account'
 10.   Verify 'ACCOUNT DELETED!' is visible

The 'registered_user' fixture (conftest.py) first creates a real account and
logs out, so there is always a valid account to log in with.
"""
from pages.login_page import LoginPage
from pages.account_page import AccountDeletedPage


def test_login_with_correct_credentials(home_page, registered_user):
    page = home_page.page

    # Steps 1-3: open the site again (the fixture left us on the login page)
    home_page.open()
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: 'Login to your account' is visible
    login_page = LoginPage(page)
    assert login_page.is_login_heading_visible()
    print("'Login to your account' is visible")

    # Steps 6-7: enter the correct email + password and click Login
    login_page.login(email=registered_user.email, password=registered_user.password)

    # Step 8: 'Logged in as username' is visible
    assert home_page.is_logged_in_as(registered_user.name)
    print(f"Logged in as {registered_user.name}")

    # Step 9: click 'Delete Account'
    home_page.delete_account()

    # Step 10: 'ACCOUNT DELETED!' is visible
    account_deleted_page = AccountDeletedPage(page)
    assert account_deleted_page.get_confirmation_text() == "ACCOUNT DELETED!"
    print("Account deleted (cleanup done)")
