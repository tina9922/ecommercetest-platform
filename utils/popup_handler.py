from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_popup(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll('[role="dialog"], .modal, .overlay')
            .forEach(el => el.remove());
        """)
    except:
        pass