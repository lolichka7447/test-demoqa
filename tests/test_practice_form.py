import pytest
import allure
from pages.practice_form_page import PracticeFormPage


@allure.feature('TextBoxPage')
@pytest.fixture(scope="function")
def practice_form_page(driver):
    page = PracticeFormPage(driver)
    with allure.step('Open Home page'):
        page.open()
    return page


def test_registration_form(driver):
    registration_page = PracticeFormPage(driver)
    registration_page.open()
    registration_page.fill_first_name("John")
    registration_page.fill_last_name("Doe")
    registration_page.fill_email("john.doe@example.com")
    registration_page.select_gender()
    registration_page.fill_mobile("1234567890")
    registration_page.fill_date_of_birth("01 Jan 1990")
