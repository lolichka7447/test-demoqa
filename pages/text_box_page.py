from pages.base_page import BasePage
from locators import TextBoxPageLocators


class TextBoxPage(BasePage):

    def open(self):
        super().open("text-box")

    def username(self):
        return self.find_element(*TextBoxPageLocators.username)

    def email(self):
        return self.find_element(*TextBoxPageLocators.email)

    def current_address(self):
        return self.find_element(*TextBoxPageLocators.current_address)

    def permanent_address(self):
        return self.find_element(*TextBoxPageLocators.permanent_address)

    def submit_button(self):
        return self.find_element(*TextBoxPageLocators.submit_button)

    def success_text_name(self):
        return self.find_element(*TextBoxPageLocators.success_text_name)

    def success_text_email(self):
        return self.find_element(*TextBoxPageLocators.success_text_email)

    def success_text_current_address(self):
        return self.find_element(*TextBoxPageLocators.success_text_current_address)

    def success_text_permanent_address(self):
        return self.find_element(*TextBoxPageLocators.success_text_permanent_address)
