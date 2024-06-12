import pytest
import allure
from pages.text_box_page import TextBoxPage
from faker import Faker

fake = Faker()


@allure.feature('TextBoxPage')
@pytest.fixture(scope="function")
def textbox_page(browser):
    page = TextBoxPage(browser)
    with allure.step('Open Home page'):
        page.open()
    return page

@allure.story('Input data')
@allure.title('Input user data')
def test_reg(textbox_page):
    # username = fake.name()
    # email = fake.email()
    # current_address = fake.address()
    # permanent_address = fake.address()
    username = '111'
    email = 'test'
    current_address = 'test'
    permanent_address = 'test'

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
        success_name_text = textbox_page.success_text_name().text
        assert username in success_name_text, f"Expected {username} to be in {success_name_text}"
        success_email_text = textbox_page.success_text_email().text
        assert email in success_email_text, f"Expected {email} to be in {success_email_text}"
        success_current_address_text = textbox_page.success_text_current_address().text
        assert current_address in success_current_address_text, f"Expected {current_address} to be in {success_current_address_text}"
        success_permanent_address_text = textbox_page.success_text_permanent_address().text
        assert permanent_address in success_permanent_address_text, f"Expected {permanent_address} to be in {success_permanent_address_text}""Expected {permanent_address} to be in {success_permanent_address_text}"