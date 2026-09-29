from playwright.sync_api import playwright

class ShopPage:
    def __init__(self, page):        
        self.page = page  
           

    def add_product(self, product_name):
        self.page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.page.get_by_role("button", name="ADD TO CART").nth(2).click()
        self.page.get_by_role("img", name="Strawberry - 1/4 Kg").click()
        self.page.locator("div").filter(has_text="×Strawberry - 1/4 Kg180").nth(2).click()
        self.page.locator("div:nth-child(24) > .product-action > button").click()
        self.page.locator("div:nth-child(20) > .stepper-input > .increment").click()
        self.page.locator("div:nth-child(20) > .product-action > button").click()

    def proceed_to_checkout(self):
        self.page.get_by_role("link", name="Cart").click()
        self.page.get_by_role("button", name="PROCEED TO CHECKOUT").click()