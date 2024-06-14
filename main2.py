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
       sleep(10)
       self.driver.implicitly_wait(10)
       self.wait = WebDriverWait(self.driver, 15)


   def boot(self):
       self.driver.get(data1.WebData().url2)
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
           sleep(10)
           self.fillText(locator1.WebLocators().usernameLocator2, data1.WebData().username2)
           self.fillText(locator1.WebLocators().passwordLocator2, data1.WebData().password2)
           self.clickButton(locator1.WebLocators().buttonLocator2)
           sleep(10)


           if self.driver.current_url == data1.WebData().dashboardURL2:
               print("Successfully LoggedIn")
           else:
               print("Error in login:Invalid credentials")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()




obj = LoginPage()
obj.login()




