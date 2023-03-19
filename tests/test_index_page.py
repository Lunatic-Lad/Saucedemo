import pytest
import allure

@pytest.mark.api
@pytest.mark.smoke
@allure.description('Checking successful login with correct credentials')
@allure.label('owner', 'Vlad')
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_to_login_button()
    index_page.validate_text()

@pytest.mark.ui


def test_unsuccessful_login(index_page):
    index_page.enter_error_name()
    index_page.enter_error_password()
    index_page.click_to_login_button()
    index_page.validate_error()


def test_successful_logout(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_to_login_button()
    index_page.click_to_menu()
    index_page.click_to_logout()
    index_page.validate_logout()


def test_order(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_to_login_button()
    index_page.click_to_add_backpack()
    index_page.click_to_cart()
    index_page.click_to_checkout()
    index_page.enter_first_name()
    index_page.enter_last_name()
    index_page.enter_postal_code()
    index_page.click_to_continue()
    index_page.click_to_finish_purchase()
    index_page.validate_checkout_purchase()

