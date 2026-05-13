from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.popup_handler import close_popup
from selenium.webdriver.support.ui import WebDriverWait
from pages.checkoutpage import CheckoutPage
import time

def test_checkout_end_to_end(driver):
    #REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    print("URL after login", driver.current_url)
    
    inventory = InventoryPage(driver)
    if not inventory.is_loaded():
        raise Exception("Inventory page could not be loaded")
    print("Inventory loaded successfully")
    
    #inventory.add_item_backpack_to_cart()
    
    # 🛒 Add multiple items 
    #inventory.add_item("Sauce Labs Backpack")
    #inventory.add_item("Sauce Labs Bike Light")
    #inventory.add_item("Sauce Labs Bolt T-Shirt")
    
    items = ["Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
    
    #adding multiple items to cart  
    for item in items:
        inventory.add_item(item)
        
    #validate the badge count
    assert inventory.get_badge_count() == "3"
    print("quantity retrieved from badge")
    
    inventory.go_to_cart()
    
    cart = CartPage(driver)
    
    #cart validation
    assert cart.is_item_present("Sauce Labs Backpack") 
    assert cart.is_item_present("Sauce Labs Bike Light")
    
    #checkout
    cart.click_checkout()
    
    #fill in the details on the checkout page and click the checkout button
    
    checkout = CheckoutPage(driver)
    ''' checkout.fill_in_details("Test", "User", "12345")
    checkout.continue_checkout()
    checkout.finish() '''
    
    checkout.complete_checkout("Test", "User", "12345")
    
    print("success message ", checkout.get_success_message)
    
    
'''

Now your framework supports:

Data separation
Reusability
Clean tests
🧠 Interview-Level Explanation (VERY IMPORTANT)

If asked:

👉 “How did you design your checkout tests?”

Say:

“I implemented a layered Page Object Model with reusable business flows like complete_checkout, and used pytest parameterization to drive multiple datasets, improving coverage while keeping tests maintainable.”

💥 That answer = strong hire signal
'''