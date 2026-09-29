import re
from playwright.sync_api import expect

def test_google_title(page):   
   
    page.goto("https://www.google.com")
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill("Playwright")
    search_box.press("Enter")
    expect(page).to_have_title(re.compile(r"Playwright"))       