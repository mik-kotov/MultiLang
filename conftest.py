import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")
@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    language= request.config.getoption("language")
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207//"
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()

