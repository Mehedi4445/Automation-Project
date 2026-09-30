import os

import pytest
from playwright.sync_api import sync_playwright

from pages.home_page import HomePage
from utils.flows import register_user_from_login_page
from utils.helpers import create_user_data

# automationexercise.com shows Google ads, and sometimes a full-screen ad
# ("Vignette" ad) pops up over the page and steals whatever we try to click
# next. Blocking requests to these ad domains stops the ad from ever
# loading, so it can never get in the way of a click.
AD_DOMAINS_TO_BLOCK = [
    "**/*doubleclick.net/**",
    "**/*googlesyndication.com/**",
    "**/*googleadservices.com/**",
    "**/*google.com/pagead/**",
    "**/*google.com/ads/**",
]


@pytest.fixture
def page():
    """
    Opens one browser + one tab for each test, and closes it afterwards.
    Runs with a visible browser by default. To run without a window
    (for example on a server):   HEADLESS=1 pytest
    """
    headless = os.getenv("HEADLESS", "0") == "1"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()

        # Block ad requests so no ad popup can appear during the test
        for pattern in AD_DOMAINS_TO_BLOCK:
            page.route(pattern, lambda route: route.abort())

        yield page

        browser.close()


@pytest.fixture
def home_page(page):
    """Opens the website and returns the Home Page object, ready to use."""
    home = HomePage(page)
    home.open()
    return home


@pytest.fixture
def new_user():
    """A brand-new (NOT yet registered) user with unique name and email."""
    return create_user_data()


@pytest.fixture
def registered_user(home_page, new_user):
    """
    Creates a real account on the website, logs out, and returns the user
    details. Tests that need an existing account (e.g. Login) use this.
    """
    home_page.go_to_signup_login_page()
    register_user_from_login_page(home_page.page, new_user)
    assert home_page.is_logged_in_as(new_user.name)
    home_page.logout()
    return new_user
