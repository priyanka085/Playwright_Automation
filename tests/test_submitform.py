
from playwright.sync_api import expect


def test_submit_form(page):

    page.goto("https://rahulshettyacademy.com/angularpractice/")
    page.locator("form input[name=\"name\"]").click()
    page.locator("form input[name=\"name\"]").fill("Priy")
    page.locator("form input[name=\"name\"]").press("Tab")
    page.locator("input[name=\"email\"]").fill("priy@gmail.com")
    page.locator("input[name=\"email\"]").press("Tab")
    page.get_by_role("textbox", name="Password").fill("12345")
    page.get_by_role("checkbox", name="Check me out if you Love").check()
    page.get_by_label("Gender").select_option("Female")
    page.get_by_role("radio", name="Employed").check()
    page.locator("input[name=\"bday\"]").fill("1989-01-01")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("× Success! The Form has been")).to_be_visible()
    page.get_by_text("× Success! The Form has been").click()



