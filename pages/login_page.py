from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CLASS_NAME, "error-message-container")
    
    ''' def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 👈 add wait
        
    def load(self):
        self.driver.get(self.URL)
        
    def login(self, username, password):
        print("URL before finding element:", self.driver.current_url)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        #self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
        
    def get_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text '''
    
    def load(self):
        self.open(self.URL) 
        
    def login(self,username,password):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
    
    def wait_for_url(self,text):
        self.wait_for_url_contains(text)
     
    
    '''
    POM means one page -> one class . the page is like a real person that can do stuff
    Interviewers LOVE this answer:

👉
“Page Object Model separates test logic from UI interactions, improving maintainability and reducing duplication. 
If UI changes, I only update locators in one place.”

POM = actions
Tests = validation

Your LoginPage is basically:

👉 A reusable “robot” that knows how to:

Open login page
Enter credentials
Click login
Read errors

def __init__(self, driver):
    self.driver = driver
    
    This connects:

Your test → to this page

login_page = LoginPage(driver)

Now this page can control the browser.


Page not fully loaded (MOST LIKELY)
Why this fixes it

Without wait:
👉 Selenium runs faster than the browser

With wait:
👉 Selenium waits until element is visible before interacting

You just learned:

👉 Static waits = bad
👉 Explicit waits = industry standard

Implicit Wait (one-line global wait)
Selenium keeps trying for up to 10 seconds
As soon as element is found → continues
It waits for everything, even when not needed

Explicit Wait
Waits only for THIS element
Waits until it is visible (not just present)

    '''
    
