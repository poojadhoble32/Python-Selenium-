from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.WebBrowserConnect import BrowserConnect
import time


class CBRB:

    elementClick = (By.XPATH, "//*[text()='Elements']")
    checkBoxButton = (By.XPATH, "//span[text()='Check Box']")
    homeBox = (By.XPATH, "//*[@class='rct-collapse rct-collapse-btn']")
    desktopBox = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/button")
    notesBox = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]")
    commandsBox = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]")
    radioButtonClick = (By.XPATH, "//span[text()='Radio Button']")
    yesButton = (By.ID, 'yesRadio')
    impressiveButton = (By.ID, 'impressiveRadio')

    def elementButton(self):
        elementsbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.elementClick))
        elementsbutton.click()

    def checkBox(self):
        checkboxbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.checkBoxButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", checkboxbutton)

        homebox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.homeBox))
        BrowserConnect.driver.execute_script("arguments[0].click();", homebox)

        desktopbox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.desktopBox))
        BrowserConnect.driver.execute_script("arguments[0].click();", desktopbox)

        notesbox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.notesBox))
        BrowserConnect.driver.execute_script("arguments[0].click();", notesbox)

        commandsbox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.commandsBox))
        BrowserConnect.driver.execute_script("arguments[0].click();", commandsbox)
        time.sleep(2)

    def radioButton(self):
        radiobutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(CBRB.radioButtonClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", radiobutton)
        time.sleep(2)

        yesradiobutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(CBRB.yesButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", yesradiobutton)
        time.sleep(3)

        impressiveradiobutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(CBRB.impressiveButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", impressiveradiobutton)
        time.sleep(3)
