import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.WebBrowserConnect import BrowserConnect


class Table:

    webTableClick = (By.ID, "item-3")

    def webTableButton(self):
        webtablebutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(Table.webTableClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", webtablebutton)

    def rowSizeFind(self):
        rowsize = len(BrowserConnect.driver.find_elements(By.XPATH, "//*[@role='rowgroup']"))
        print("row size is:",rowsize)

    def colSizeFind(self):
        colsize = len(BrowserConnect.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group'][1]/div/div"))
        print("col size is:", colsize)

    def TableLoop(self):
        for row in range(1, 4):
            firstname = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[1]"))))
            print("FirstName is :", firstname.text)

            lastname = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[2]"))))
            print("LastName is :", lastname.text)

            age = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[3]"))))
            print("age is :", age.text)

            email = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[4]"))))
            print("email id is :", email.text)

            salary = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[5]"))))
            print("salary is :", salary.text)

            department = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[6]"))))
            print("department is :", department.text)

            action = WebDriverWait(BrowserConnect.driver, 5).until(
                (EC.presence_of_element_located((By.XPATH, f"//div[@class='rt-tr-group'][{row}]/div/div[7]"))))
            print("action is :", action.text)

            time.sleep(2)
