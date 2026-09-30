"""
Test Case 3: Login User with incorrect email and password
Steps:
 1-3.  Launch browser, open the site, verify home page is visible
 4.    Click 'Signup / Login'
 5.    Verify 'Login to your account' is visible
 6-7.  Enter incorrect email and password, click 'Login'
 8.    Verify error 'Your email or password is incorrect!' is visible
"""
from pages.login_page import LoginPage


def test_login_with_incorrect_credentials(home_page):
    page = home_page.page

    # Step 3: home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: 'Login to your account' is visible
    login_page = LoginPage(page)
    assert login_page.is_login_heading_visible()
    print("'Login to your account' is visible")

    # Steps 6-7: try logging in with an account that does not exist
    login_page.login(email="not_a_real_user_123@example.com", password="wrongPassword123")

    # Step 8: verify the error message
    assert login_page.get_login_error_text() == "Your email or password is incorrect!"
    print("Correct error message shown for invalid login")
