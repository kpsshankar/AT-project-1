"""
loginPage.py
"""


from Data1 import data1
from Locator1 import locator1
from time import sleep


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.implicitly_wait(10)
       self.wait = WebDriverWait(self.driver, 15)


   def boot(self):
       self.driver.get(data1.WebData().url4)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()


   def fillText(self, locator, value):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(value)


   def clickButton(self, locator):
       self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()


   def login(self):
       try:
           self.boot()
           self.fillText(locator1.WebLocators().usernameLocator4, data1.WebData().username4)
           self.fillText(locator1.WebLocators().passwordLocator4, data1.WebData().password4)
           self.clickButton(locator1.WebLocators().buttonLocator4_1)
           sleep(10)
           self.clickButton(locator1.WebLocators().buttonLocator4_2)
           self.clickButton(locator1.WebLocators().buttonLocator4_3)
           self.fillText(locator1.WebLocators().EmployeeNameLocator4, data1.WebData().EmployeeName4)
           sleep(10)
           self.clickButton(locator1.WebLocators().searchLocator4_4)
           self.clickButton(locator1.WebLocators().selectLocator4_5)
           self.clickButton(locator1.WebLocators().buttonLocator4_6)
           self.clickButton(locator1.WebLocators().editLocator4_7)
           self.fillText(locator1.WebLocators().EmployeeFirstNameLocator4, data1.WebData().EmployeeFirstName4)
           self.fillText(locator1.WebLocators().EmployeeIdLocator4, data1.WebData().EmployeeId4)
           sleep(10)
           self.clickButton(locator1.WebLocators().saveLocator4)
           sleep(10)


           if self.driver.current_url != data1.WebData().dashboardURL4:
               print("Existing  user has Successfully Edited")
           else:
               print("Existing  User Details Edition Failed")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()

obj = LoginPage()
obj.login()




