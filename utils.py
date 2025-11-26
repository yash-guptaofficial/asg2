from selenium.webdriver.support.ui import Select
import time


class WaitUtils:
    @staticmethod
    def wait(seconds):
        time.sleep(seconds)

    @staticmethod
    def wait_for_milliseconds(milliseconds):
        time.sleep(milliseconds / 1000)


class SelectUtils:
    @staticmethod
    def select_by_value(element, value):
        select = Select(element)
        select.select_by_value(value)

    @staticmethod
    def select_by_visible_text(element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    @staticmethod
    def select_by_index(element, index):
        select = Select(element)
        select.select_by_index(index)


class AssertionUtils:
    @staticmethod
    def assert_text_contains(actual_text, expected_text, message=""):
        assert expected_text.lower() in actual_text.lower(), f"Expected text '{expected_text}' not found in '{actual_text}'. {message}"

    @staticmethod
    def assert_element_visible(is_visible, element_name="Element"):
        assert is_visible, f"{element_name} is not visible"

    @staticmethod
    def assert_equal(actual, expected, message=""):
        assert actual == expected, f"Expected {expected}, but got {actual}. {message}"

    @staticmethod
    def assert_greater_than(actual, value, message=""):
        assert actual > value, f"Expected value greater than {value}, but got {actual}. {message}"
