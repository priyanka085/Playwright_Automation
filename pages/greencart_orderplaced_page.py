from playwright.sync_api import expect
class OrderPlacedPage:
    def __init__(self, page):
        self.page = page
        expect(self.page.get_by_text("Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"))

    def verify_order_placed_page(self):
        expect(self.page.get_by_text("Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!")).to_be_visible()
