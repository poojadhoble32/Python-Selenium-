from selenium import webdriver


class BrowserConnect:

    driver = None

    def openChrome(self):

        BrowserConnect.driver = webdriver.Chrome()
        BrowserConnect.driver.maximize_window()
        BrowserConnect.driver.get("https://demoqa.com/books")

    def driverClose(self):
        BrowserConnect.driver.close()
