from base_object.base import BaseObject
from base_object.locators import Locators
import allure


class IndexPage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("entering user-name")
    def enter_user_name(self):
        self.type_keys(Locators.USERNAME_FIELD, "standard_user")

    @allure.step("entering password")
    def enter_password(self):
        self.type_keys(Locators.PASSWORD_FIELD, "secret_sauce")

    @allure.step("clicking to login button")
    def click_to_login_button(self):
        self.click(Locators.LOGIN_BTN)

    @allure.step("validate title text")
    def validate_text(self):
        self.assertion(self.get_text(Locators.TITLE), "Products")

    def validate_error(self):
        self.assertion(self.get_text(Locators.ERROR_MESSAGE), "Epic sadface: Username and password do not match any "
                                                              "user in this service")

    def enter_error_name(self):
        self.type_keys(Locators.USERNAME_FIELD, "standard_error")

    def enter_error_password(self):
        self.type_keys(Locators.PASSWORD_FIELD, "secret_error")

    def click_to_menu(self):
        self.click(Locators.MENU)

    def click_to_logout(self):
        self.click(Locators.LOGOUT)

    def validate_logout(self):
        self.assertion(self.get_text(Locators.LOGO_NAME), "Swag Labs")

    def click_to_add_backpack(self):
        self.click(Locators.SAUCE_LABS_BACKPACK)

    def click_to_cart(self):
        self.click(Locators.CART)

    def click_to_checkout(self):
        self.click(Locators.CHECKOUT)

    def enter_first_name(self):
        self.type_keys(Locators.FIRST_NAME, 'Vladislav')

    def enter_last_name(self):
        self.type_keys(Locators.LAST_NAME, 'Baidiuk')

    def enter_postal_code(self):
        self.type_keys(Locators.POSTAL_CODE, '366666')

    def click_to_continue(self):
        self.click(Locators.CONTINUE_BTN)

    def click_to_finish_purchase(self):
        self.click(Locators.FINISH_PURCHASE)

    def validate_checkout_purchase(self):
        self.assertion(self.get_text(Locators.CHECKOUT_SUCCESSFUL_ORDER), "Thank you for your order!")



