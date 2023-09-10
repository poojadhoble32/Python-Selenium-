from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.WebBrowserConnect import BrowserConnect
from selenium.webdriver.common.alert import Alert
import time


class Switches:

    afwButton = (By.XPATH, "//*[text()='Alerts, Frame & Windows']")
    browserButton = (By.XPATH, "//*[text()='Browser Windows']")
    newTabClick = (By.ID, 'tabButton')
    newWindowClick = (By.ID, 'windowButton')
    newWindowMsgClick = (By.ID, 'messageWindowButton')
    framesButton = (By.XPATH, "//span[text()='Frames']")
    frame2Element = (By.XPATH, '//*[@id="sampleHeading"]')
    frame1Element = (By.XPATH, '//*[@id="sampleHeading"]')
    alertClick = (By.XPATH, "//span[text()='Alerts']")
    buttonAlert = (By.ID, "alertButton")
    timeClick = (By.ID, "timerAlertButton")
    confirmClick = (By.ID, 'confirmButton')
    promptClick = (By.ID, 'promtButton')
    fID1 = "frame1"
    fID2 = "frame2"
    parentwindow = None
    defaultframe = None

    def afwButtonClick(self):
        afwbuttonclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.afwButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", afwbuttonclick)

    def browserWindowClick(self):
        browserwindowclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.browserButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", browserwindowclick)

    def parentID(self):
        # get parent window handle before clicking on new window button
        Switches.parentwindow = BrowserConnect.driver.current_window_handle

    def newTabSwitch(self):

        # click on new window button
        newtabbuttonclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.newTabClick))
        newtabbuttonclick.click()

        # get handle of all opened windows
        windows = BrowserConnect.driver.window_handles

        # loop over all windows, and if window is not parent window, switch to that window
        for childwindow in windows:
            if childwindow != Switches.parentwindow:
                BrowserConnect.driver.switch_to.window(childwindow)

        BrowserConnect.driver.switch_to.window(Switches.parentwindow)

    def newWindowSwitch(self):
        # click on new window button
        newwindowbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.newWindowClick))
        newwindowbutton.click()

        # get handle of all opened windows
        windows = BrowserConnect.driver.window_handles

        # loop over all windows, and if window is not parent window, switch to that window
        for childwindow in windows:
            if childwindow != Switches.parentwindow:
                BrowserConnect.driver.switch_to.window(childwindow)

        BrowserConnect.driver.switch_to.window(Switches.parentwindow)

    def newWindowMsgSwitch(self):

        # click on new window button
        newwindowmsgbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.newWindowMsgClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", newwindowmsgbutton)

        # get handle of all opened windows
        windows = BrowserConnect.driver.window_handles

        # loop over all windows, and if window is not parent window, switch to that window
        for childwindow in windows:
            if childwindow != Switches.parentwindow:
                BrowserConnect.driver.switch_to.window(childwindow)

        BrowserConnect.driver.switch_to.window(Switches.parentwindow)

    def frameSwitch(self):
        framesclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.framesButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", framesclick)

    def frameDefault(self):
        BrowserConnect.driver.switch_to.default_content()

    def frame1Switch(self):

        BrowserConnect.driver.switch_to.frame(Switches.fID1)
        frame1 = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Switches.frame1Element))
        print(frame1.text)

    def frame2Switch(self):
        BrowserConnect.driver.switch_to.frame(Switches.fID2)
        frame2 = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Switches.frame2Element))
        print(frame2.text)

    def alertButtonClick(self):
        alertbuttonclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.alertClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", alertbuttonclick)

    def buttonAlertSwitch(self):
        buttonalert = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.buttonAlert))
        buttonalert.click()
        alert = Alert(BrowserConnect.driver)
        alert.accept()

    def TimeAlertSwitch(self):
        timeralertclick = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.timeClick))
        timeralertclick.click()
        time.sleep(6)
        alert1 = Alert(BrowserConnect.driver)
        alert1.accept()

    def confirmAlertSwitch(self):
        confirmalert = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.confirmClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", confirmalert)
        alert2 = Alert(BrowserConnect.driver)
        alert2.accept()
        # alert2.dismiss()

    def promptAlertSwitch(self):
        promptalert = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Switches.promptClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", promptalert)
        alert3 = Alert(BrowserConnect.driver)
        alert3.send_keys("Pooja Dhoble")
        alert3.accept()
