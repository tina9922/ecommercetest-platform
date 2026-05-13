import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkoutpage import CheckoutPage
from pages.cart_page import CartPage

@pytest.mark.parametrize(
    
    "first,last,zip_code",
    [
        ("John", "Doe", "12345"),
        ("Alice", "Smith", "98765"),
        ("Bob", "Lee", "560001"),  
    ]
)

def test_checkout_multiple_users(driver, first, last, zip_code):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    print("URL after login", driver.current_url)
    
    inventory = InventoryPage(driver)
    if not inventory.is_loaded():
        raise Exception("Inventory page could not be loaded")
    print("Inventory loaded successfully")
    
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
    checkout.complete_checkout(first,last,zip_code)
    
    print("success message ", checkout.get_success_message())