from selenium.webdriver.support.select import Select


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_at(self, locator, data):
        self.get_element(locator).send_keys(data)

    def selected_by_value(self, locator, value):
        select = Select(self.get_element(locator))
        select.select_by_value(value)

    def is_selected(self, locator):
        return self.get_element(locator).is_selected()
