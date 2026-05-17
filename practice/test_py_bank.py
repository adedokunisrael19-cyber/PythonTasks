from unittest import TestCase

import py_bank

class TestValidateEmail(TestCase):

    def test_that_validates_email_function_exist (self):
        py_bank.validate_email("kayode.gem@gmail.com")
    def test_that_validate_email_passwword_has_minimum_of_8_characters(self):
        is_valid = py_bank.validate_email("kayom@gmail.com")
        self.assertTrue(is_valid)
    def test_that_validate_email_passwword_is_less_than_8_characters_returns_false(self):
        is_valid =  py_bank.validate_email("kayom@i")
        self.assertFalse(is_valid)
    def test_that_validate_email_password_has_special_characters(self):
        self.assertRaises(ValueError, py_bank.validate_email, "kayomgmail.com")
