from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.AccountPage import AccountPage
from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
# @pytest.mark.skipif(reason='when test is failed')
class TestLogin:
    def test_search_for_valid_credentials(self):
        home_page=HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("amotooricap9@gmail.com","12345")
        assert account_page.edit_your_account_information_option_link_text

    def test_search_for_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_timestamp(),"1234")
        assert login_page.warning_message_for_invalid_credentials_xpath

    def test_search_for_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_timestamp(), "12345")
        assert login_page.warning_message_for_invalid_credentials_xpath

    def test_without_entering_creds(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        assert login_page.warning_message_for_invalid_credentials_xpath

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        print(time_stamp)
        return "amotoori"+time_stamp+"@gmail.com"