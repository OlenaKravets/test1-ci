from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(3)
    assert "Google" in driver.title
    driver.quit()
