from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.WebBrowserConnect import BrowserConnect


class Login(BrowserConnect):

    loginButton = (By.ID, 'login')
    usernameTextBox = (By.ID, 'userName')
    passwordTextBox = (By.ID, 'password')
    finalLoginButtonClick = (By.XPATH, "//button[@id='login' and @type='button']")
    invalidUnamePass = (By.ID, 'name')
    loginSuccessButton = (By.ID, "submit")
    blankUserNameError = (By.XPATH, "//*[@id='userName' and @class = 'mr-sm-2 is-invalid form-control']")
    blankPasswordError = (By.XPATH, "//*[@id='password' and @class = 'mr-sm-2 is-invalid form-control']")

    def __init__(self):
        BrowserConnect.__init__(self)

    def loginButtonClick(self):
        loginbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.loginButton))
        loginbutton.click()

    def sendUsername(self, username):
        unametextbox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.usernameTextBox))
        unametextbox.clear()
        unametextbox.send_keys(username)

    def sendPassword(self, password):
        passwordbox = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.passwordTextBox))
        passwordbox.clear()
        passwordbox.send_keys(password)

    def finalLoginButton(self):
        finalloginbutton = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.finalLoginButtonClick))
        # due to error of selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element is not clickable
        BrowserConnect.driver.execute_script("arguments[0].click();", finalloginbutton)

    def loginSuccess(self):
        WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.loginSuccessButton))

    def invalidUnamePassword(self):
        invalidunamepass = WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.invalidUnamePass))
        return invalidunamepass.text

    def blankPassword(self):
        WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.blankPasswordError))

    def blankUname(self):
        WebDriverWait(BrowserConnect.driver, 10).until(
            EC.presence_of_element_located(Login.blankUserNameError))
