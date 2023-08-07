"""
Page object for DuckDuckGo result page.
"""


class DuckDuckGoSearchPage:

    def __int__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        return ""

    def search_input_value(self):
        return ""

    def title(self):
        return ""