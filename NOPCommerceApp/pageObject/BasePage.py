# from selenium.webdriver.common.by import By
#
#
# class BasePage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def type_into_element(self,text,locator):
#         element = self.get_element(locator)
#         element.click()
#         element.clear()
#         element.send_keys(text)
#
#     def element_click(self,locator):
#         element = self.get_element(locator)
#         element.click()
#
#     def get_element(self,locator):
#         element = None
#         if locator.__contains__("_id"):
#             element = self.driver.find_element(By.ID, locator)
#         elif locator.__contains__("_name"):
#             element = self.driver.find_element(By.NAME, locator)
#         elif locator.__contains__("_class_name"):
#             element = self.driver(By.CLASS_NAME, locator)
#         elif locator.__contains__("_link_text"):
#             element = self.driver(By.LINK_TEXT, locator)
#         elif locator.__contains__("_xpath"):
#             element = self.driver(By.XPATH, locator)
#         elif locator.__contains__("_css"):
#             element = self.driver.find_element(By.CSS_SELECTOR, locator)
#
#         return element
#
#     def check_display_status_of_element(self,locator):
#         element = self.get_element(locator)
#         return element.is_displayed()
#
#     def retreive_element_text(self,locator):
#         element = self.get_element(locator)
#         return element.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, text, locator):
        element = self.get_element(locator)
        if element:
            element.click()
            element.clear()
            element.send_keys(text)
        else:
            print(f"Element not found with locator: {locator}")

    def element_click(self, locator):
        element = self.get_element(locator)
        if element:
            element.click()
        else:
            print(f"Element not found with locator: {locator}")

    def get_element(self, locator, timeout=10):
        try:
            if "_id" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, locator)))
            elif "_name" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, locator)))
            elif "_class_name" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
            elif "_link_text" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
            elif "_xpath" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            elif "_css" in locator:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except Exception as e:
            print(f"Error finding element with locator: {locator}. Exception: {str(e)}")
        return None

    def check_display_status_of_element(self, locator):
        element = self.get_element(locator)
        if element:
            return element.is_displayed()
        else:
            print(f"Element not found with locator: {locator}")
            return False

    def retrieve_element_text(self, locator):
        element = self.get_element(locator)
        if element:
            return element.text
        else:
            print(f"Element not found with locator: {locator}")
            return None
