import pytest
import allure

from pages.text_box_page import TextBoxPage
from faker import Faker


@allure.feature('TextBoxPage')
@pytest.fixture(scope="function")
def textbox_page(driver):
    page = TextBoxPage(driver)
    with allure.step('Open Home page'):
        page.open()
    return page


@allure.story('Input data')
@allure.title('Input user data')
def test_reg(textbox_page):
    fake = Faker()
    username = fake.name()
    email = fake.email()
    current_address = fake.address()
    permanent_address = fake.address()

    with allure.step('Enter user data'):
        with allure.step('Enter username'):
            textbox_page.username().send_keys(username)
        with allure.step('Enter email'):
            textbox_page.email().send_keys(email)
        with allure.step('Enter current address'):
            textbox_page.current_address().send_keys(current_address)
        with allure.step('Enter permanent address'):
            textbox_page.permanent_address().send_keys(permanent_address)

    with allure.step('Submit button'):
        textbox_page.submit_button().click()

    with allure.step('Verify success message'):
        assert username in textbox_page.success_text_name().text, \
            f"Expected '{username}' to be in '{textbox_page.success_text_name().text}'"

        assert email in textbox_page.success_text_email().text, \
            f"Expected '{email}' to be in '{textbox_page.success_text_email().text}'"

        # Убираем переносы строк и пробелы до и после адреса
        assert current_address.replace('\n', ' ') in textbox_page.success_text_current_address().text.replace('\n',
                                                                                                              ' '), \
            f"Expected '{current_address}' to be in '{textbox_page.success_text_current_address().text}'"

        assert permanent_address.replace('\n', ' ') in textbox_page.success_text_permanent_address().text.replace('\n',
                                                                                                                  ' '), \
            f"Expected '{permanent_address}' to be in '{textbox_page.success_text_permanent_address().text}'"
