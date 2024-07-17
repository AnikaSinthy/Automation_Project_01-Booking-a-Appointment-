import time
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://katalon-demo-cura.herokuapp.com/")
        self.driver.maximize_window()
        time.sleep(2)
        print("setup_complete")

    def tearDown(self):
        self.driver.close()
        print("Complete")

    def test_print(self):
        print("Hi")