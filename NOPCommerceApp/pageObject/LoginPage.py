from selenium.webdriver.common.by import By

from pageObject.AccountPage import AccountPage


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email_address_field="input-email"
    password_field_id="input-password"
    login_button_xpath="//input[@value='Login']"
    warning_message_for_invalid_credentials_xpath="//*[contains(text(), 'Warning: No match for E-Mail Address and/or Password.')]"

    def enter_email_address(self,email_address_text):
        self.driver.find_element(By.ID,self.email_address_field).click()
        self.driver.find_element(By.ID, self.email_address_field).clear()
        self.driver.find_element(By.ID, self.email_address_field).send_keys(email_address_text)

    def enter_password(self,password_text):
        self.driver.find_element(By.ID,self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return AccountPage(self.driver)

    def verify_message_for_invalid_credentials(self):
        return self.driver.find_element(By.XPATH,self.warning_message_for_invalid_credentials_xpath).is_displayed()
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

    def login_to_application(self,email_address_text,password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_login()
