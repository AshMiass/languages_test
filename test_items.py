import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestItems():
    def test_should_present_add_to_basket_button(self, browser):
        browser.get(link)
        btns = browser.find_elements_by_css_selector(".btn-add-to-basket")
        assert len(btns) == 1