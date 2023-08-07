"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():

    # Initialize the ChromeDriver instance
    b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Wait up to 10 seconds for the elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()