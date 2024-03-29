import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language_name', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_name)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()



