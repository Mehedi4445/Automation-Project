import random
import re
import time
from dataclasses import dataclass


def generate_unique_email():
    """
    Creates a new email address every time (current time in milliseconds
    plus a small random number), so registering never fails with
    'Email Address already exist!' when a test is run again.
    """
    unique_number = int(time.time() * 1000)
    return f"testuser{unique_number}{random.randint(10, 99)}@example.com"


def generate_random_name():
    """Creates a simple random name like 'User4821'."""
    return f"User{random.randint(1000, 9999)}"


def price_to_number(price_text: str) -> int:
    """
    Turns a price shown on the website into a number, so we can do maths.
    Example: 'Rs. 500' -> 500     'Rs. 1,200' -> 1200
    """
    return int(re.sub(r"\D", "", price_text))


@dataclass
class UserData:
    """All the details needed to register one user. One object = one user."""
    name: str
    email: str
    password: str = "Test@1234"
    birth_day: str = "10"
    birth_month: str = "5"
    birth_year: str = "1995"
    first_name: str = ""
    last_name: str = "Tester"
    company: str = "Test Company"
    address1: str = "123 Test Street"
    address2: str = "Suite 45"
    country: str = "United States"
    state: str = "Texas"
    city: str = "Austin"
    zipcode: str = "12345"
    mobile_number: str = "1234567890"


def create_user_data() -> UserData:
    """Builds a brand-new user with a random name and a unique email."""
    name = generate_random_name()
    return UserData(name=name, email=generate_unique_email(), first_name=name)
