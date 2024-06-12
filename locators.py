from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    username = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    permanent_address = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    success_text_name = (By.ID, "name")
    success_text_email = (By.ID, "email")
    success_text_current_address = (By.ID, "currentAddress")
    success_text_permanent_address = (By.ID, "permanentAddress")
