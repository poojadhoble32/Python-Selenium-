from WebPages.LoginPage import Login
from WebPages.WebBrowserConnect import BrowserConnect
from WebPages.Switches import Switches
from WebPages.DropDown import DropDown
from WebPages.CheckBoxRadioButton import CBRB
from WebPages.Table import Table


class LoginPageTest:

    login = Login()
    connectObj = BrowserConnect()
    switch = Switches()
    dropdown = DropDown()
    CBRBobj = CBRB()
    table = Table()

    def commonSuccessLogin(self):
        LoginPageTest.connectObj.openChrome()
        LoginPageTest.login.loginButtonClick()
        LoginPageTest.login.sendUsername('pooja_pokharkar')
        LoginPageTest.login.sendPassword("Pooja@1234")
        LoginPageTest.login.finalLoginButton()

    def LoginSuccessTest(self):
        LoginPageTest.connectObj.openChrome()
        LoginPageTest.login.loginButtonClick()
        LoginPageTest.login.sendUsername('pooja_pokharkar')
        LoginPageTest.login.sendPassword("Pooja@1234")
        LoginPageTest.login.finalLoginButton()
        print("Login Successfull")
        LoginPageTest.connectObj.driverClose()

    def invalidUsernamePassTest(self):
        LoginPageTest.connectObj.openChrome()
        LoginPageTest.login.loginButtonClick()
        LoginPageTest.login.sendUsername('pooja_pokharkar')
        LoginPageTest.login.sendPassword("Pooja@12345")
        LoginPageTest.login.finalLoginButton()
        result = LoginPageTest.login.invalidUnamePassword()
        print(result)
        LoginPageTest.connectObj.driverClose()

    def blankPasswordTest(self):
        LoginPageTest.connectObj.openChrome()
        LoginPageTest.login.loginButtonClick()
        LoginPageTest.login.sendUsername('pooja_pokharkar')
        LoginPageTest.login.sendPassword('')
        LoginPageTest.login.finalLoginButton()
        LoginPageTest.login.blankPassword()
        print("Please fill password")
        LoginPageTest.connectObj.driverClose()

    def blankUnameTest(self):
        LoginPageTest.connectObj.openChrome()
        LoginPageTest.login.loginButtonClick()
        LoginPageTest.login.sendUsername('')
        LoginPageTest.login.sendPassword("Pooja@1234")
        LoginPageTest.login.finalLoginButton()
        LoginPageTest.login.blankUname()
        print("Please fill Username")
        LoginPageTest.connectObj.driverClose()

    def windowSwitchTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.switch.afwButtonClick()
        LoginPageTest.switch.browserWindowClick()
        LoginPageTest.switch.parentID()
        LoginPageTest.switch.newTabSwitch()
        print("New Tab Switched")
        LoginPageTest.switch.newWindowSwitch()
        print("New Window Switched")
        LoginPageTest.switch.newWindowMsgSwitch()
        print("New Window Message Switched")
        LoginPageTest.connectObj.driverClose()

    def frameSwitchTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.switch.afwButtonClick()
        LoginPageTest.switch.frameSwitch()
        LoginPageTest.switch.frame1Switch()
        LoginPageTest.switch.frameDefault()
        LoginPageTest.switch.frame2Switch()
        LoginPageTest.switch.frameDefault()
        LoginPageTest.connectObj.driverClose()

    def alertSwitchTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.switch.afwButtonClick()
        LoginPageTest.switch.alertButtonClick()
        LoginPageTest.switch.buttonAlertSwitch()
        LoginPageTest.switch.TimeAlertSwitch()
        LoginPageTest.switch.confirmAlertSwitch()
        LoginPageTest.switch.promptAlertSwitch()
        LoginPageTest.connectObj.driverClose()

    def dropDownTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.dropdown.widgetButtonClick()
        LoginPageTest.dropdown.selectButtonClick()
        LoginPageTest.dropdown.selectValueDD()
        LoginPageTest.dropdown.pageSource()
        LoginPageTest.dropdown.selectOneDD()
        LoginPageTest.dropdown.oldSelectDD()
        LoginPageTest.dropdown.multiSelectDD()
        LoginPageTest.dropdown.standardMultiSelect()
        LoginPageTest.connectObj.driverClose()

    def CheckBoxTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.CBRBobj.elementButton()
        LoginPageTest.CBRBobj.checkBox()
        LoginPageTest.connectObj.driverClose()

    def radioButtonTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.CBRBobj.elementButton()
        LoginPageTest.CBRBobj.radioButton()
        LoginPageTest.connectObj.driverClose()

    def tableTest(self):
        LoginPageTest.commonSuccessLogin(self)
        LoginPageTest.CBRBobj.elementButton()
        LoginPageTest.table.webTableButton()
        LoginPageTest.table.rowSizeFind()
        LoginPageTest.table.colSizeFind()
        LoginPageTest.table.TableLoop()
        LoginPageTest.connectObj.driverClose()
