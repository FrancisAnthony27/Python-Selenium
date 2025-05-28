import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or use Firefox, Edge etc.
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
