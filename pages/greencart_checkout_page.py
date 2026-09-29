class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def verify_checkout_page(self):
        pass
    def proceed_to_place_order(self):
        self.page.get_by_role("button", name="Place Order").click()
        