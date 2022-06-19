from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_TO_CART_NAME_BOOK = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_PRICE_IN_THE_CART = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')