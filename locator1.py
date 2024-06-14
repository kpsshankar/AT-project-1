"""
locator.py
"""
class WebLocators:


   def __init__(self):
   #AT_project1:TC_Login_01
       self.usernameLocator1 = "//input[@placeholder='Username']"
       self.passwordLocator1 = "//input[@placeholder='Password']"
       self.buttonLocator1 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
   #AT_project1:TC_Login_02
       self.usernameLocator2 = "//input[@placeholder='Username']"
       self.passwordLocator2 = "//input[@placeholder='Password']"
       self.buttonLocator2 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
   # AT_project1:TC_PIM_01
       self.usernameLocator3 = "//input[@placeholder='Username']"
       self.passwordLocator3 = "//input[@placeholder='Password']"
       self.buttonLocator3_1 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.buttonLocator3_2 = "//span[text()='PIM']"
       self.buttonLocator3_3 = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
       self.FirstNameLocator3 = "//input[@placeholder='First Name']"
       self.MiddleNameLocator3 = "//input[@placeholder='Middle Name']"
       self.LastNameLocator3 = "//input[@placeholder='Last Name']"
       self.EmployeeIdLocator3 = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
       self.buttonLocator3_4 = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
   # AT_project1:TC_PIM_02
       self.usernameLocator4 = "//input[@placeholder='Username']"
       self.passwordLocator4 = "//input[@placeholder='Password']"
       self.buttonLocator4_1 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.buttonLocator4_2 = "//span[text()='PIM']"
       self.buttonLocator4_3 = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a"
       self.EmployeeNameLocator4 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
       self.searchLocator4_4 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
       self.selectLocator4_5 = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i"
       self.buttonLocator4_6 = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i"
       self.editLocator4_7 = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i"
       #self.EmployeeFirstNameLocator4 = "//input[@placeholder='First name']"
       self.EmployeeFirstNameLocator4  ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
       self.EmployeeIdLocator4 = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"
       self.saveLocator4      = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
   # AT_project1:TC_PIM_03
       self.usernameLocator5 = "//input[@placeholder='Username']"
       self.passwordLocator5 = "//input[@placeholder='Password']"
       self.loginLocator5_1 = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.PIMLocator5_2 = "//span[text()='PIM']"
       self.EmployeelistLocator5 = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a"
       self.EmployeeNameLocator5 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
       self.searchLocator5_3 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
       self.selectLocator5_4 = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span/i"
       self.DeleteLocator5_5   = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i"
       self.YesDelete5        = "/html/body/div/div[3]/div/div/div/div[3]/button[2]"