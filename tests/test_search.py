"""
Tests covering DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['zebra', 'python', 'arctic fox'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searched for "zebra"
    search_page.search(phrase)

    # Then the search result query is "zebra"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "zebra"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "zebra"
    assert phrase in result_page.title()
