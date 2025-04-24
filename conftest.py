import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="Choose browser language"
    )

# Фикстура для получения параметра
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nStart browser with language: {user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()