"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import json


@pytest.fixture()
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture()
def browser(config):

    # Initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif config['browser'] == 'Chrome':
        b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config['browser'] == 'Headless Chrome':  # test fail in this mode! need to work on that
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]} is not supported')

    # Wait up to 10 seconds for the elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
