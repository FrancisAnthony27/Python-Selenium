class UploadPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path):
        upload_input = self.driver.find_element("id", "file-upload")
        upload_input.send_keys(file_path)

    def submit_file(self):
        self.driver.find_element("id", "file-submit").click()

    def get_success_text(self):
        return self.driver.find_element("tag name", "h3").text
