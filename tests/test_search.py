"""
Tests covering DuckDuckGo searches.
"""


from pages.result import DuckDuckGoSearchPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoSearchPage(browser)
    PHRASE = "zebra"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searched for "zebra"
    search_page.search(PHRASE)

    # Then the search result title contains "zebra"
    assert PHRASE == result_page.title()

    # And the search result query is "zebra"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "zebra"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # TODO: Remove this exception once the test is complete
    raise Exception("Incomplete Test")
