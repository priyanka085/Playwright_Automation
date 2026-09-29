from pages.mobile_home_page import MobileHomePage


def test_order_mobile(page):

    mobile_home_page = MobileHomePage(page)
    mobile_home_page.init_page()
    mobile_home_page.add_phone_to_cart(phone_name="iphone X $24.99 Lorem ipsum")
    mobile_home_page.add_phone_to_cart(phone_name="Nokia Edge $24.99 Lorem ipsum")
    mobile_home_page.add_phone_to_cart(phone_name="Blackberry $24.99 Lorem ipsum")
    mobile_home_page.proceed_to_checkout()
    mobile_home_page.complete_purchase()
    mobile_home_page.verify_success_message()
