from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CartPage(BasePage):
    
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID,"checkout")
    
    def get_cart_items_names(self):
        elements = self.wait.until(lambda d: d.find_elements(*self.ITEM_NAME))
        return [el.text for el in elements]
    
    def is_item_present(self,item_name):
        return item_name in self.get_cart_items_names()
    
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        
        
