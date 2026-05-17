from unittest import TestCase 

import py_banks

class TestValidateEmail(TestCase):

    def test_that_validate_email_exists(self):
        py_banks.validate_email("my@mail.com")
    def test_that_validate_email_has_a_minimum_of_8_characters(self):
        is_valid=py_banks.validate_email("adedokun@email.com")
        self.assertTrue(is_valid)
    def test_that_validate_email_has_less_than_8_characters(self):
        is_valid=py_banks.validate_email("a.@com")
        self.assertFalse(is_valid)
    def that_validate_email_does_not_have_special_characters(self):
        self.assertRaises(ValueError,validate_email,"adedokun@email.com")
    def test_that_validates_email_does_not_start_or_end_with_special_characters(self):
        is_valid = py_banks.validate_email("@adeoluwa@gmail")
        self.assertFalse(is_valid)
    #def test_that_validates_email_does_not_start_or_end_with_special_characters(self):
