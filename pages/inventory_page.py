from pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class InventoryPage(BasePage):
    
    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEM = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    # Wait for page to load
    def is_loaded(self):
        return self.find(self.INVENTORY_CONTAINER)
    
    def add_item_backpack_to_cart(self):
        self.click((self.INVENTORY_ITEM)) 
        
    def add_item(self,item_name):
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.click((By.XPATH, xpath))
               
    ''' def add_item_multiple_times(self,item_name,qty):
        for i in range(qty):
            print(f"Adding {item_name} - iteration {i+1}")
            self.add_item(item_name)      
         '''
    def go_to_cart(self):
        self.click(self.CART_ICON)
        
    def get_badge_count(self):
        return self.get_text(self.CART_BADGE)
    
