from selenium.webdriver.common.by import By

from pageObject.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.retrieve_element_text(self.no_product_message_xpath)

    def retreive_no_product_message(self):
        return self.retrieve_element_text(self.no_product_message_xpath)