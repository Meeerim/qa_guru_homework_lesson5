import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    browser.config.window_width = 1400
    browser.config.window_height = 700

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 2.0

