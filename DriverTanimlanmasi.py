from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate(self, url):
        self.driver.get(url)

    def search(self, text):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(text)
        search_box.submit()

    def close(self):
        self.driver.quit()