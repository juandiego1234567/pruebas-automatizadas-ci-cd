import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Tipo de navegador: Chrome, Firefox, Edge" )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f'Browser {browser} no soportado')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    login = LoginPage(driver)
    return login

@pytest.fixture
def product_page(driver):
    producto = ProductPage(driver)
    return producto


