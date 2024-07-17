import os
import time

from locators.locators import Locators
from Page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def click_make_appointment(self):
        self.click_element(self.locator.Make_Appointment)
        time.sleep(2)

    def enter_name(self, name):
        self.enter_at(self.locator.User_Name, name)

    def enter_password(self, password):
        self.enter_at(self.locator.Password, password)

    def click_login(self):
        self.click_element(self.locator.Login)

    def select_facility(self, value):
        self.selected_by_value(self.locator.Facility, value)

    def select_apply(self):
        self.click_element(self.locator.Apply)

    def assert_apply(self):
        value = self.is_selected(self.locator.Apply)
        print(value)
        return value

    def select_medicare(self):
        self.click_element(self.locator.medicare)

    def assert_medicare(self):
        value = self.is_selected(self.locator.medicare)
        print(value)
        return value

    def select_medicaid(self):
        self.click_element(self.locator.medicaid)

    def assert_medicaid(self):
        value = self.is_selected(self.locator.medicaid)
        print(value)
        return value

    def select_none(self):
        self.click_element(self.locator.none)

    def enter_visit(self, visit):
        self.enter_at(self.locator.Visit, visit)

    def enter_comment(self, comment):
        self.enter_at(self.locator.comment, comment)

    def click_booking(self):
        self.click_element(self.locator.booking)


