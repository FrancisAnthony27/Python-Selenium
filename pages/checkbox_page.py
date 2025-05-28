class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://the-internet.herokuapp.com/checkboxes")

    def get_checkboxes(self):
        return self.driver.find_elements("css selector", "input[type='checkbox']")

    def validate_checkboxes(self):
        checkboxes = self.get_checkboxes()
        return not checkboxes[0].is_selected() and checkboxes[1].is_selected()
