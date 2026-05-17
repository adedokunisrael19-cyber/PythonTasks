from unittest import TestCase

import practice_work

class TestValidateEmail(TestCase):
    def Test_that_validat_email(self):
        practice_work.validate_email("adedokun@gmail.com")

    def test_that_validate_email_length_is_minimum_than_8(self):
        isValid = practice_work.validate_email("adedokun@gmail.com")
        self.assertTrue(isValid)

#    def test_that_validate_email_length_is_less_than_8(self):
#        isValid = practice_work.validate_email("adom")
#        self.assertFalse(isValid)
       
    def test_that_validate_email_contains_special(self):
        
        self.assertRaises(ValueError,practice_work.validate_email,"adedokungmail.com"  )

    def test_that_validate_email_contains_special_characters(self):
        isValid = practice_work.validate_email("adecokun@gmail.com")
        self.assertTrue(isValid)

class TestCalculateBalance(TestCase):
    def test_calculate_balance(self):
        actual = practice_work.calculate_balance([2500, 3000])
        expected = 5500
        self.assertEqual(actual, expected)
        
    def test_that_calculate_when_5000_is_deposited(self):
        actual = practice_work.calculate_balance([5000, 3000])
        expected = 8000
        self.assertEqual(actual, expected)



