from pages.login_page import LoginPage
from utils.popup_handler import close_popup

def test_valid_login(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    #print(driver.current_url)
    #time.sleep(10) # 👈 pause to see the page
    login_page.wait_for_url("inventory")
       
''' def test_debug(driver):
    driver.get("https://www.saucedemo.com/")
    print(driver.title) '''
    
'''
Where is driver coming from?

This line in your test:

def test_valid_login(driver):

👉 means PyTest is injecting driver automatically from a fixture.
Flow of Execution

PyTest sees:

def test_valid_login(driver):
It looks for a fixture named driver
Finds it in conftest.py

Runs:

driver = webdriver.Chrome()
Passes that driver into your test

After test finishes:

driver.quit()
driver → comes from fixture
passed into LoginPage(driver)
used inside your Page Object

So somewhere in your project, you should have a file like:

conftest.py


FLAKY TEST PROBLEM
Adding test_debug() method introduced an extra browser navigation and extra time delay. this means that the framework had a timing issue.
root cause is that the login() runs too fast after the load(). Even though i used wait, the page was not fully ready

Interview-ready explanation

If asked:

“Why did your test start passing after adding/removing another test?”

You can say:

The test had a timing issue where the page wasn't fully loaded before interacting with elements. 
Adding another test temporarily introduced delay, masking the issue. 
I fixed it properly by adding explicit waits to ensure element readiness, making the test stable.

structure becomes:

pages/
  base_page.py   👈 reusable engine
  login_page.py  👈 specific page

tests/
  test_login.py  👈 only business logic
'''