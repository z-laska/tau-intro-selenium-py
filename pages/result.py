"""
Page object for DuckDuckGo result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

    RESULT_LINKS = (By.CSS_SELECTOR, '[data-testid="result-title-a"]')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __int__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        return ""

    def search_input_value(self):
        return ""

    def title(self):
        return ""