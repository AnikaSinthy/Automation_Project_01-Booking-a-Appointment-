import time
from Test.base_test import BaseTest
from Page.home_page import HomePage
from data.data import TestData as DATA


class TestCase(BaseTest):
    def test_appointment(self):
        tc = HomePage(self.driver)
        tc.click_make_appointment()
        time.sleep(2)
        tc.enter_name(DATA.name)
        tc.enter_password(DATA.password)
        tc.click_login()
        tc.select_facility(DATA.value)
        tc.select_apply()
        tc.select_medicare()
        assert tc.assert_medicare() == True
        time.sleep(2)
        tc.enter_visit(DATA.visit)
        tc.enter_comment(DATA.comment)
        time.sleep(2)
        tc.click_booking()

    def test_with_different_value(self):
        tc = HomePage(self.driver)
        tc.click_make_appointment()
        time.sleep(2)
        tc.enter_name(DATA.name)
        tc.enter_password(DATA.password)
        tc.click_login()
        tc.select_facility(DATA.value)
        tc.select_apply()
        tc.select_medicaid()
        assert tc.assert_medicaid() == True
        time.sleep(2)
        tc.enter_visit(DATA.visit_1)
        tc.enter_comment(DATA.comment_1)
        time.sleep(2)
        tc.click_booking()

    def test_wrong_name(self):
        tc = HomePage(self.driver)
        tc.click_make_appointment()
        time.sleep(2)
        tc.enter_name(DATA.name_1)
        tc.enter_password(DATA.password)
        tc.click_login()
        tc.select_facility(DATA.value)
        tc.select_apply()
        tc.select_medicare()
        assert tc.assert_medicare() == True
        time.sleep(2)
        tc.enter_visit(DATA.visit)
        tc.enter_comment(DATA.comment_1)
        time.sleep(2)
        tc.click_booking()

    def test_wrong_password(self):
        tc = HomePage(self.driver)
        tc.click_make_appointment()
        time.sleep(2)
        tc.enter_name(DATA.name)
        tc.enter_password(DATA.password_1)
        tc.click_login()
        tc.select_facility(DATA.value)
        tc.select_apply()
        tc.select_medicare()
        assert tc.assert_medicare() == True
        time.sleep(2)
        tc.enter_visit(DATA.visit_1)
        tc.enter_comment(DATA.comment)
        time.sleep(2)
        tc.click_booking()
