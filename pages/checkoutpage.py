from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CheckoutPage(BasePage):
    FIRSTNAME = (By.ID,"first-name")
    LASTNAME = (By.ID,"last-name")
    POSTALCODE = (By.ID,"postal-code")
    CONTINUE = (By.ID,"continue")
    FINISH = (By.ID,"finish")
    COMPLETE_HEADER = (By.CLASS_NAME,"complete-header")
    
    
    def fill_in_details(self,first,last,zip):
        self.type(self.FIRSTNAME,first)
        self.type(self.LASTNAME,last)
        self.type(self.POSTALCODE,zip)
    
    def continue_checkout(self):
        self.click(self.CONTINUE)
        
    def finish(self):
        self.click(self.FINISH)
        
        # -------- Validations -------- #
        
    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)
    
    def complete_checkout(self,first,last,zip_code):
        """
        High-level business flow (very senior pattern)
        """
        self.fill_in_details(first,last,zip_code)
        self.continue_checkout()
        self.finish()
    
    '''
    Why this is senior-level
Low-level + high-level methods both exist
Test can call:
granular steps OR
one business flow (complete_checkout)

👉 This is how real frameworks are designed
    '''
        
        
    
    