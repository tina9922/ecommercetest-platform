from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def open(self,url):
        self.driver.get(url)

    def find(self,locator):
        print("Trying to find:", locator)
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self,locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            raise Exception(f"failed to click on {locator}:{str(e)}")
            
        
    def type(self,locator,text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self,locator):
        return self.find(locator).text
    
    def wait_for_url_contains(self,text):
        self.wait.until(lambda d: text in d.current_url)
        print("assertion succeeded")
    
'''
A senior SDET:

Eliminates duplication
Handles waits (no flaky tests)
Abstracts Selenium details
Designs reusable components

If interviewer asks:

👉 “How did you design your framework?”

Say:

“I implemented a layered Page Object Model using a BasePage abstraction to encapsulate Selenium interactions, 
added explicit waits to reduce flakiness and improve test relaibility, and separated test logic from UI actions to improve maintainability and scalability and to avoid duplication.”

Interview Line (Use This)

“I automated an end-to-end add-to-cart workflow using a layered Page Object Model, 

validating UI state through cart badge updates and item verification in the cart page.”

Interview gold:

“I added custom error handling for better debugging”

Your Resume Value Just Jumped

Now you can say:

Built a scalable automation framework with UI and API testing layers integrated into a CI/CD pipeline using GitHub Actions.

💥 That answer = senior SDET

self.wait = WebDriverWait(driver, 10)

So it will wait up to 10 seconds. it will keep checking the condition until it becomes true -> test continues, timeout happens and the test fails

lambda d: text in d.current_url

This is the condition function:

d = your WebDriver instance
d.current_url = current page URL
text in d.current_url = checks if substring exists

login_page.wait_for_url_contains("inventory")
it makes the test relaible and non-flaky
What this does step-by-step:
You click login
App starts navigating to next page
Instead of immediately checking (which can fail), you wait

Selenium keeps checking:

Is "inventory" in current URL?
Once it becomes true → test proceeds

'''