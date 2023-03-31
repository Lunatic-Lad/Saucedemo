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


case_1 = ["incorrect", "incorrect", "Epic sadface: Username and password do not match any user in this service"]
case_2 = ["", "", "Epic sadface: Username is required"]
case_3 = ["locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."]

@pytest.mark.api
@pytest.mark.smoke
@allure.description('Checking successful login with incorrect credentials')
@allure.label('owner', 'Vlad')
@allure.title('Unsuccessful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("error_name, error_password, error_message", (case_1, case_2, case_3), ids=["Incorrect_password", "Empty_username", "Locked_out_user"])
def test_unsuccessful_login(index_page, error_name, error_password, error_message):
    index_page.enter_error_name(error_name)
    index_page.enter_error_password(error_password)
    index_page.click_to_login_button()
    index_page.validate_error(error_message)

@pytest.mark.api
@allure.description('Checking successful logout from site')
@allure.label('owner', 'Vlad')
@allure.title('Successful logout')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_logout(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_to_login_button()
    index_page.click_to_menu()
    index_page.click_to_logout()
    index_page.validate_logout()

@pytest.mark.api
@allure.description('Checking a successful order')
@allure.label('owner', 'Vlad')
@allure.title('Successful order')
@allure.suite('Order suite')
@allure.severity(allure.severity_level.BLOCKER)
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

