from pages.checkbox_page import CheckboxPage

def test_checkboxes(driver):
    page = CheckboxPage(driver)
    page.load()
    assert page.validate_checkboxes()
