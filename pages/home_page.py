from playwright.sync_api import Page

BASE_URL = "https://www.automationexercise.com"


class HomePage:
    """
    Represents the Home Page (https://www.automationexercise.com/).
    All the navbar links live here because almost every test starts
    by clicking one of these links.
    """

    def __init__(self, page: Page):
        self.page = page

        # Navbar links
        # NOTE: the page repeats some of these same links elsewhere (e.g. a
        # "View Cart" link inside a hidden popup), so we scope every locator
        # to the navbar itself (".navbar-nav") to always match exactly one
        # element. ".first" is an extra safety net.
        navbar = page.locator(".navbar-nav")
        self.signup_login_link = navbar.locator('a[href="/login"]').first
        self.products_link = navbar.locator('a[href="/products"]').first
        self.cart_link = navbar.locator('a[href="/view_cart"]').first

        # Shown only after a successful login
        self.logged_in_as_text = navbar.locator("li:has-text('Logged in as')")
        self.logout_link = navbar.locator('a[href="/logout"]')
        self.delete_account_link = navbar.locator('a[href="/delete_account"]')

        # Home page content
        self.slider = page.locator("#slider")
        self.product_items = page.locator(".features_items .product-image-wrapper")

    def open(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_timeout(2000)

    def is_home_page_visible(self) -> bool:
        """The big slider/banner at the top only exists on the home page."""
        return self.slider.first.is_visible()

    # ---------- Navigation ----------

    def go_to_signup_login_page(self):
        self.signup_login_link.click()
        self.page.wait_for_timeout(2000)

    def go_to_products_page(self):
        self.products_link.click()
        self.page.wait_for_timeout(2000)

    def go_to_cart_page(self):
        self.cart_link.click()
        self.page.wait_for_timeout(2000)

    # ---------- Products shown on the home page ----------

    def click_view_product_by_index(self, index: int = 0):
        """Clicks 'View Product' under a product card (first = 0)."""
        self.product_items.nth(index).locator("a:has-text('View Product')").click()
        self.page.wait_for_timeout(2000)

    # ---------- Logged-in actions ----------

    def is_logged_in_as(self, name: str) -> bool:
        return self.logged_in_as_text.inner_text().strip() == f"Logged in as {name}"

    def logout(self):
        self.logout_link.click()
        self.page.wait_for_timeout(2000)

    def delete_account(self):
        self.delete_account_link.click()
        self.page.wait_for_timeout(2000)
