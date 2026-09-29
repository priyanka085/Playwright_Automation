class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.page.get_by_role("combobox")
        self.page.get_by_role("checkbox")
        self.page.get_by_role("button", name="Proceed")

    def verify_payment_page(self):
        pass

    def proceed_to_payment(self):
        self.page.get_by_role("combobox").select_option("Canada")
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Proceed").click()
       