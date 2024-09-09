import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage

class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    baseURL="https://flipkart.com"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # time.sleep(10)
        act_title = self.driver.title
        print("*******************")
        print(act_title)

        if act_title == "Amazon.com":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
