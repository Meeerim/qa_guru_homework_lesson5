import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1400
    browser.config.window_height = 700

    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0


