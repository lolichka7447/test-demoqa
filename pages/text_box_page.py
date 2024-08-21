from pages.base_page import BasePage
from locators import TextBoxPageLocators as TB


class TextBoxPage(BasePage):

    def open(self):
        super().open("text-box")

    def username(self):
        return self.find_element(*TB.USERNAME)

    def email(self):
        return self.find_element(*TB.EMAIL)

    def current_address(self):
        return self.find_element(*TB.CURRENT_ADDRESS)

    def permanent_address(self):
        return self.find_element(*TB.PERMANENT_ADDRESS)

    def submit_button(self):
        return self.find_element(*TB.SUBMIT_BUTTON)

    def success_text_name(self):
        return self.find_element(*TB.SUCCESS_TEXT_NAME)

    def success_text_email(self):
        return self.find_element(*TB.SUCCESS_TEXT_EMAIL)

    def success_text_current_address(self):
        return self.find_element(*TB.SUCCESS_TEXT_CURRENT_ADDRESS)

    def success_text_permanent_address(self):
        return self.find_element(*TB.SUCCESS_TEXT_PERMANENT_ADDRESS)
