from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math



class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        link.click()

    def check_name_boock_in_the_cart(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        add_name_book = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_NAME_BOOK).text
        assert name_book == add_name_book, "There is not that book in the cart"

    def check_book_price_in_the_cart(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_the_cart = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_THE_CART).text
        print(book_price, book_price_in_the_cart)
        assert book_price in book_price_in_the_cart, "There is wrong price in the cart"




