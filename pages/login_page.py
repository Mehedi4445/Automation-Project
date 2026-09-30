from playwright.sync_api import Page


class LoginPage:
    """
    Represents the 'Login / Signup' page (https://www.automationexercise.com/login).
    This one page has two forms side by side: Login form and Signup form.
    """

    def __init__(self, page: Page):
        self.page = page

        # Login form (left side)
        self.login_heading = page.locator("h2:has-text('Login to your account')")
        self.login_email = page.locator('input[data-qa="login-email"]')
        self.login_password = page.locator('input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')
        self.login_error_message = page.locator(".login-form p")

        # Signup form (right side)
        self.signup_heading = page.locator("h2:has-text('New User Signup!')")
        self.signup_name = page.locator('input[data-qa="signup-name"]')
        self.signup_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')
        self.signup_error_message = page.locator(".signup-form p")

    # ---------- Checks ----------

    def is_login_heading_visible(self) -> bool:
        return self.login_heading.is_visible()

    def is_signup_heading_visible(self) -> bool:
        return self.signup_heading.is_visible()

    # ---------- Reusable functions ----------

    def login(self, email: str, password: str):
        """Fills the login form and clicks the Login button."""
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(2000)

    def start_signup(self, name: str, email: str):
        """
        Fills the small signup form (name + email) and clicks 'Signup'.
        This takes the user to the 'Enter Account Information' page.
        """
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()
        self.page.wait_for_timeout(2000)

    def get_login_error_text(self) -> str:
        return self.login_error_message.inner_text().strip()

    def get_signup_error_text(self) -> str:
        return self.signup_error_message.inner_text().strip()
