from selenium.webdriver.common.by import By


class Locators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    MENU = (By.ID, 'react-burger-menu-btn')
    LOGOUT = (By.ID, 'logout_sidebar_link')
    LOGO_NAME = (By.CLASS_NAME, "login_logo")
    SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CSS_SELECTOR, "#root .primary_header div:nth-child(3)")
    CHECKOUT = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_PURCHASE = (By.ID, "finish")
    CHECKOUT_SUCCESSFUL_ORDER = (By.CSS_SELECTOR, "#root .complete-header")
