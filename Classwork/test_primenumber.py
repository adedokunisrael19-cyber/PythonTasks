from unittest import TestCase

import primenumber

class TestValidateNumber(TestCase):

    def test_that_validates_number (self):
        primenumber.isPrime(16)

    def test_that_validates_number_is_prime(self):
        isvalid = primenumber.isPrime(12)
        self.assertFalse(isvalid)  

    def test_that_validates_number_is_not_prime(self):
        isvalid = primenumber.isPrime(11)
        self.assertTrue(isvalid)
 




