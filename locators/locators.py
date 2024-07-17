from selenium.webdriver.common.by import By


class Locators():
    Make_Appointment = By.ID, "btn-make-appointment"
    User_Name = By.ID, "txt-username"
    Password = By.ID, "txt-password"
    Login = By.ID, "btn-login"
    Facility = By.ID, "combo_facility"
    Apply = By.ID, "chk_hospotal_readmission"
    medicare = By.ID, "radio_program_medicare"
    medicaid = By.ID, "radio_program_medicaid"
    none = By.ID, "radio_program_none"
    Visit = By.ID, "txt_visit_date"
    comment = By.ID, "txt_comment"
    booking = By.ID, "btn-book-appointment"



