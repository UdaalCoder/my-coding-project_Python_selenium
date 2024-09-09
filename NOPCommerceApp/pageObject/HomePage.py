# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from pageObject.BasePage import BasePage
# from pageObject.LoginPage import LoginPage
# from pageObject.SearchPage import SearchPage
#
#
# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     search_box_field_name = "search"
#     search_button_xpath = "//button[contains(@class,'btn-default')]"
#     my_account_drop_menu = "//span[contains(text(), 'My Account')]"
#     login_option = "Login"
#
#     def enter_product_into_search_box_field(self, product_name):
#         self.type_into_element(product_name, self.search_box_field_name)
#
#     def click_on_search_button(self):
#         self.element_click(self.search_button_xpath)
#         return SearchPage(self.driver)
#
#     def click_on_my_account_drop_men(self):
#         self.element_click(self.my_account_drop_menu)
#
#     def select_login_option(self):
#         self.element_click(self.login_option)
#         return LoginPage(self.driver)
#
#     def search_for_a_product(self, product_name):
#         self.enter_product_into_search_box_field(product_name)
#         self.click_on_search_button()
#
#     def navigate_to_login_page(self):
#         self.click_on_my_account_drop_men()
#         return self.select_login_option()

from selenium.webdriver.common.by import By
from pageObject.BasePage import BasePage
from pageObject.LoginPage import LoginPage
from pageObject.SearchPage import SearchPage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu = "//span[contains(text(), 'My Account')]"
    login_option = "Login"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click(self.search_button_xpath)  # Corrected method call
        return SearchPage(self.driver)  # Correctly returning SearchPage object

    def click_on_my_account_drop_menu(self):
        self.element_click(self.my_account_drop_menu)

    def select_login_option(self):
        self.element_click(self.login_option)
        return LoginPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()  # Make sure to return the SearchPage object


