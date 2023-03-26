from base_object.base import BaseObject
from base_object.locators import Locators
from support.assertion import Assertions
import allure


class IndexPage(BaseObject, Assertions):
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


    @allure.step("validate error message")
    def validate_error(self, error_message):
        self.assertion(self.get_text(Locators.ERROR_MESSAGE), error_message)

    @allure.step("validate error name")
    def enter_error_name(self, error_name):
        self.type_keys(Locators.USERNAME_FIELD, error_name)

    @allure.step("validate error password")
    def enter_error_password(self, error_password):
        self.type_keys(Locators.PASSWORD_FIELD, error_password)

    @allure.step("clicking to menu button")
    def click_to_menu(self):
        self.click(Locators.MENU)

    @allure.step("clicking to logout button")
    def click_to_logout(self):
        self.click(Locators.LOGOUT)

    @allure.step("validate logout")
    def validate_logout(self):
        self.assertion(self.get_text(Locators.LOGO_NAME), "Swag Labs")

    @allure.step("clicking to add backpack")
    def click_to_add_backpack(self):
        self.click(Locators.SAUCE_LABS_BACKPACK)

    @allure.step("adding to cart")
    def click_to_cart(self):
        self.click(Locators.CART)

    @allure.step("clicking to checkout")
    def click_to_checkout(self):
        self.click(Locators.CHECKOUT)

    @allure.step("entering first-name")
    def enter_first_name(self):
        self.type_keys(Locators.FIRST_NAME, 'Vladislav')

    @allure.step("entering last-name")
    def enter_last_name(self):
        self.type_keys(Locators.LAST_NAME, 'Baidiuk')

    @allure.step("entering postal-code")
    def enter_postal_code(self):
        self.type_keys(Locators.POSTAL_CODE, '366666')

    @allure.step("clicking to continue")
    def click_to_continue(self):
        self.click(Locators.CONTINUE_BTN)

    @allure.step("clicking to finish purchase")
    def click_to_finish_purchase(self):
        self.click(Locators.FINISH_PURCHASE)

    @allure.step("clicking to checkout purchase")
    def validate_checkout_purchase(self):
        self.assertion(self.get_text(Locators.CHECKOUT_SUCCESSFUL_ORDER), "Thank you for your order!")
