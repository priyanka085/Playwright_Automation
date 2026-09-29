from utils.config import mobile_home_url
from playwright.sync_api import Playwright, expect

class MobileHomePage:
    def __init__(self, page):
        self.page = page
        self.items_count = 0
    
    def init_page(self):
        self.page.goto(mobile_home_url)
        self.page.get_by_role("link", name="Shop").click()
   
    def add_phone_to_cart(self, phone_name):
        self.page.locator("app-card").filter(has_text=phone_name).get_by_role("button").click()
        self.items_count += 1
       
    def proceed_to_checkout(self):
        self.page.get_by_text(f"Checkout ( {self.items_count} ) (current)").click()
        self.page.get_by_role("button", name="Checkout").click()

    def complete_purchase(self):        
        self.page.get_by_role("textbox", name="Please choose your delivery").click()
        self.page.get_by_role("textbox", name="Please choose your delivery").press_sequentially("in")
        self.page.get_by_text("India").click()
        self.page.get_by_text("I agree with the term &").click()
        self.page.get_by_role("button", name="Purchase").click()

    def verify_success_message(self):
        expect(self.page.get_by_text("Success!")).to_be_visible()