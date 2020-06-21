import unittest
import math

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import numbers_and_strings

class TestNumbersAndStrings(unittest.TestCase):

    def test_mean(self):
        self.assertAlmostEqual(numbers_and_strings.mean(0.2, 0.4), 0.3, places=5)
        self.assertAlmostEqual(numbers_and_strings.mean(5, 7), 6, places=5)
        self.assertAlmostEqual(numbers_and_strings.mean(0, 0), 0, places=5)

    def test_concat_digits(self):
        self.assertIsInstance(numbers_and_strings.concat_digits(1, 0), int)
        self.assertEqual(numbers_and_strings.concat_digits(1, 0), 10)
        self.assertEqual(numbers_and_strings.concat_digits(1, 1), 11)
        self.assertEqual(numbers_and_strings.concat_digits(123, 456), 123456)
        self.assertEqual(numbers_and_strings.concat_digits(0, 0), 0)

    def test_count_digits(self):
        self.assertEqual(numbers_and_strings.count_digits(123), 3)
        self.assertEqual(numbers_and_strings.count_digits(0), 1)
        self.assertEqual(numbers_and_strings.count_digits(999999), 6)

    def test_calc_three_times_n_plus_one(self):
        self.assertEqual(numbers_and_strings.calc_three_times_n_plus_one(3), 10)
        self.assertEqual(numbers_and_strings.calc_three_times_n_plus_one(5), 16)
        self.assertEqual(numbers_and_strings.calc_three_times_n_plus_one(0), 1)

    def test_my_round(self):
        self.assertIsInstance(numbers_and_strings.my_round(0.6), int)
        self.assertEqual(numbers_and_strings.my_round(0.6), 1)
        self.assertEqual(numbers_and_strings.my_round(1.2), 1)
        self.assertEqual(numbers_and_strings.my_round(3.5), 4)

    def test_is_divisible(self):
        self.assertFalse(numbers_and_strings.is_divisible(10,3))
        self.assertTrue(numbers_and_strings.is_divisible(10,5))
        self.assertTrue(numbers_and_strings.is_divisible(11,1))
        self.assertTrue(numbers_and_strings.is_divisible(100,10))

        for i in range(2,11):
            self.assertFalse(numbers_and_strings.is_divisible(11,i))

    def test_gcd(self):
        self.assertEqual(numbers_and_strings.gcd(2, 3), 1)
        self.assertEqual(numbers_and_strings.gcd(12, 6), 6)
        self.assertEqual(numbers_and_strings.gcd(13, 17), 1)
        self.assertEqual(numbers_and_strings.gcd(120, 36), 12)
    
    def test_radians(self):
        self.assertAlmostEqual(numbers_and_strings.radians(0), 0, places=5)
        self.assertAlmostEqual(numbers_and_strings.radians(90), math.pi/2, places=5)
        self.assertAlmostEqual(numbers_and_strings.radians(180), math.pi, places=5)
        
    def test_close_enough(self):
        self.assertTrue(numbers_and_strings.close_enough(1, 1.001, 0.01))
        self.assertTrue(numbers_and_strings.close_enough(0.999, 1.0, 0.01))
        self.assertFalse(numbers_and_strings.close_enough(0.9, 1.0, 0.01))
        

    def test_hypotenuse(self):
        self.assertEqual(numbers_and_strings.hypotenuse(3, 4), 5)
        self.assertEqual(numbers_and_strings.hypotenuse(-4, -3), 5)
        self.assertAlmostEqual(numbers_and_strings.hypotenuse(5, 6), math.sqrt(25+36))

    def test_binary(self):
        self.assertEqual(numbers_and_strings.binary(3), '11')
        self.assertEqual(numbers_and_strings.binary(15), '1111')
        self.assertEqual(numbers_and_strings.binary(16), '10000')
        
    def test_line(self):
        self.assertEqual(numbers_and_strings.line(0), '')
        self.assertEqual(numbers_and_strings.line(3), '---')
        self.assertEqual(numbers_and_strings.line(10), '----------')

    def test_dice(self):
        nrs = set()

        # let's throw a thousand times and see if we get all numbers
        # this might fail :-) just to keep it simple
        for i in range(1000):
            nrs.add(numbers_and_strings.dice())
        
        self.assertEqual(nrs, {1, 2, 3, 4, 5, 6})

        
if __name__ == '__main__':
    unittest.main()