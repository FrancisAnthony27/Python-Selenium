import os
from selenium import webdriver

def test_file_upload(driver):
    driver.get("http://the-internet.herokuapp.com/upload")
    
    file_path = os.path.abspath("test_upload.txt")  # <-- This makes the path absolute
    driver.find_element("id", "file-upload").send_keys(file_path)
    driver.find_element("id", "file-submit").click()
    
    success_text = driver.find_element("tag name", "h3").text
    assert success_text == "File Uploaded!"
