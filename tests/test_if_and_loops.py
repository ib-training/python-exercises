import unittest
import math

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import if_and_loops

class TestIfAndLoops(unittest.TestCase):

    def test_max(self):
        self.assertEqual(5,   if_and_loops.max(3, 5))
        self.assertEqual(5,   if_and_loops.max(5, 3))
        self.assertEqual(-10, if_and_loops.max(-10, -12))
        self.assertEqual(1.2, if_and_loops.max(1.1, 1.2))
        self.assertEqual(5,   if_and_loops.max(5, 5))

    def test_fizzbuzz(self):
        self.assertEqual(
            [
                '1', '2', 'fizz', '4', 'buzz', 'fizzbuzz', 'fizzbuzz', 'fizz', '34'
            ],
            [
                if_and_loops.fizzbuzz(1), 
                if_and_loops.fizzbuzz(2), 
                if_and_loops.fizzbuzz(3), 
                if_and_loops.fizzbuzz(4), 
                if_and_loops.fizzbuzz(5),
                if_and_loops.fizzbuzz(15),
                if_and_loops.fizzbuzz(30),
                if_and_loops.fizzbuzz(33),
                if_and_loops.fizzbuzz(34)   
            ]
        )
        
    def test_summation_while(self):
        self.assertEqual(55, if_and_loops.summation_while(1, 10))
        self.assertEqual(0, if_and_loops.summation_while(-2, 2))
        self.assertEqual(0, if_and_loops.summation_while(5, 3))
        self.assertEqual(3+4+5, if_and_loops.summation_while(3, 5))

    def test_summation_for(self):
        self.assertEqual(55, if_and_loops.summation_for(1, 10), 55)
        self.assertEqual(0, if_and_loops.summation_for(-2, 2), 0)
        self.assertEqual(0, if_and_loops.summation_for(5, 3), 0)
        self.assertEqual(3 + 4 + 5, if_and_loops.summation_for(3, 5))

       
    def test_is_vowel(self):
        self.assertTrue(if_and_loops.is_vowel('a'))
        self.assertTrue(if_and_loops.is_vowel('e'))
        self.assertTrue(if_and_loops.is_vowel('i'))
        self.assertTrue(if_and_loops.is_vowel('u'))
        self.assertTrue(if_and_loops.is_vowel('u'))
        self.assertTrue(if_and_loops.is_vowel('A'))
        self.assertTrue(if_and_loops.is_vowel('E'))
        self.assertTrue(if_and_loops.is_vowel('I'))
        self.assertTrue(if_and_loops.is_vowel('O'))
        self.assertTrue(if_and_loops.is_vowel('U'))
        self.assertFalse(if_and_loops.is_vowel('?'))
        self.assertFalse(if_and_loops.is_vowel('M'))
        self.assertFalse(if_and_loops.is_vowel('B'))

    def test_count_vowels(self):
        self.assertEqual(5, if_and_loops.count_vowels('aeiou'), 5)
        self.assertEqual(5, if_and_loops.count_vowels('AEIOU'), 5)
        self.assertEqual(0, if_and_loops.count_vowels('BKXT'), 0)
        self.assertEqual(5, if_and_loops.count_vowels('abcdefghijklmnopqrstuvwxyz'), 5)

    def test_palindrome(self):
        self.assertTrue(if_and_loops.palindrome(""))
        self.assertTrue(if_and_loops.palindrome("a"))
        self.assertTrue(if_and_loops.palindrome("anna"))
        self.assertTrue(if_and_loops.palindrome("reger"))
        self.assertTrue(if_and_loops.palindrome("abcdcba"))
        self.assertTrue(if_and_loops.palindrome("abcdcba"))
        
        self.assertFalse(if_and_loops.palindrome("abcd"))
        self.assertFalse(if_and_loops.palindrome("xyz"))
        self.assertFalse(if_and_loops.palindrome("abb")) 

    def test_three_n_plus_one(self):
        self.assertEqual([1], if_and_loops.three_n_plus_one(1))
        self.assertEqual([2, 1], if_and_loops.three_n_plus_one(2))
        self.assertEqual([3, 10, 5, 16, 8, 4, 2, 1], if_and_loops.three_n_plus_one(3))
        self.assertEqual([4, 2, 1], if_and_loops.three_n_plus_one(4))
        self.assertEqual([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], if_and_loops.three_n_plus_one(7), )
            
if __name__ == '__main__':
    unittest.main()