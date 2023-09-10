from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.WebBrowserConnect import BrowserConnect
from selenium.webdriver.support.ui import Select
import time


class DropDown:

    widgetClick = (By.XPATH, "//*[text()='Widgets']")
    selectValue = (By.XPATH, "//*[text()='Select Option']")
    selectButton = (By.XPATH, "//*[text()='Select Menu']")
    selectValueOption = (By.XPATH, "//*[text()='A root option']")
    selectOne = (By.XPATH, "//*[text()='Select Title']")
    selectOneOption = (By.XPATH, f"//*[@id='react-select-3-option-0-{1}']")
    oldSelectButton = (By.ID, 'oldSelectMenu')
    multiSelectDropDown = (By.XPATH, "//*[text()='Select...']")
    multiSelectOptions = (By.XPATH, "//*[@id='react-select-4-option-1']")
    multiSelectOption = (By.XPATH, "//*[@id='react-select-4-option-2']")
    standardMSelect = (By.ID, 'cars')

    def widgetButtonClick(self):
        widgetsbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.widgetClick))
        BrowserConnect.driver.execute_script("arguments[0].click();", widgetsbutton)

    def selectButtonClick(self):
        selectbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.selectButton))
        BrowserConnect.driver.execute_script("arguments[0].click();", selectbutton)

    def pageSource(self):
        pagesource = BrowserConnect.driver.page_source
        # in without select tag find pagesource. create its .html file open in brouser and find element
        print(pagesource)

    def selectValueDD(self):
        selectvalue = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.selectValue))
        selectvalue.click()

        selectvalueoption = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.selectValueOption))
        BrowserConnect.driver.execute_script("arguments[0].click();", selectvalueoption)

    def selectOneDD(self):
        selectone = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.selectOne))
        selectone.click()
        time.sleep(5)
        selectoneoption = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.element_to_be_clickable(DropDown.selectOneOption))
        BrowserConnect.driver.execute_script("arguments[0].click();", selectoneoption)

    def oldSelectDD(self):
        oldselectbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(DropDown.oldSelectButton))
        oldselectobj = Select(oldselectbutton)

        # select by text in select options.text is present outside of tag
        oldselectobj.select_by_visible_text('Blue')
        time.sleep(5)

        # select by value present in select options.values in select options are present inside tag
        oldselectobj.select_by_value('4')
        time.sleep(5)

        # select by index of item. index starts from 0
        oldselectobj.select_by_index(5)
        time.sleep(5)

    def multiSelectDD(self):
        multiselectdropdown = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(DropDown.multiSelectDropDown))
        multiselectdropdown.click()

        multiselectdropdownoptions = WebDriverWait(BrowserConnect.driver, 10).until(
           EC.presence_of_element_located(DropDown.multiSelectOptions))
        multiselectdropdownoptions.click()


        multiselectoptions = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(DropDown.multiSelectOption))
        multiselectoptions.click()

    def standardMultiSelect(self):
        standardmultiselect = Select(WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(DropDown.standardMSelect)))

        if standardmultiselect.is_multiple:
            standardmultiselect.select_by_index(2)
            time.sleep(2)
            standardmultiselect.select_by_index(3)
            time.sleep(2)
