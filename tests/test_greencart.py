from playwright.sync_api import expect

from pages.greencart_checkout_page import CheckoutPage
from pages.greencart_orderplaced_page import OrderPlacedPage
from pages.greencart_shop_page import ShopPage
from pages.greenvart_payment_page import PaymentPage

def test_greencart_title(page):
    shop_page = ShopPage(page)
    shop_page.add_product(page)
    shop_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.verify_checkout_page()
    checkout_page.proceed_to_place_order()

    payment_page = PaymentPage(page)
    payment_page.verify_payment_page()
    payment_page.proceed_to_payment()

    order_placed_page = OrderPlacedPage(page)
    order_placed_page.verify_order_placed_page()
       
