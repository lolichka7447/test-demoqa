from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    USERNAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUCCESS_TEXT_NAME = (By.ID, "name")
    SUCCESS_TEXT_EMAIL = (By.ID, "email")
    SUCCESS_TEXT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress.mb-1")
    SUCCESS_TEXT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress.mb-1")


class PracticeFormPageLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
