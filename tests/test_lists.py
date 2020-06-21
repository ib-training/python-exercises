import unittest
import math
import numpy as np

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import lists

class TestLists(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(lists.sum([1,2,3,4,5,6,7,8,9,10]), 55)
        self.assertEqual(lists.sum([-1, 0, 1]), 0)
        self.assertEqual(lists.sum([1,3,5,7]), 16)
        self.assertEqual(lists.sum([]), 0)

    def test_mean(self):
        self.assertEqual(lists.mean([1,2,3,4,5,6,7,8,9,10]), 5.5)
        self.assertEqual(lists.mean([1,2,3]), 2.0)
        self.assertEqual(lists.mean([1]), 1.0)

    def test_variance(self):
        random_numbers = np.random.rand(10)
        self.assertAlmostEqual(
            lists.variance(list(random_numbers)), 
            random_numbers.var(), 
            places=5
        )

        self.assertAlmostEqual(
            lists.variance([1,2,3]), 
            2/3, 
            places=5
        )
        
        self.assertAlmostEqual(
            lists.variance([1,2,3,4,5]), 
            2.0, 
            places=5
        )
        

    def test_reverse_list(self):
        self.assertEqual(lists.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_reverse_string(self):
        self.assertEqual(lists.reverse_string("foobar"), "raboof")

    def test_histogram(self):
        self.assertEqual(lists.histogram([2, 5, 1]), '##\n#####\n#')

    def test_get_word_lengths(self):
        text = "Three tomatoes are walking down the street"
        self.assertEqual(lists.get_word_lengths(text), [5, 8, 3, 7, 4, 3, 6])

    def test_find_longest_word(self):
        text = "Three tomatoes are walking down the street"
        self.assertEqual(lists.find_longest_word(text), "tomatoes")
        text = "foo foo1 foo2 foo3"
        self.assertEqual(lists.find_longest_word(text), "foo1")


    def test_validate_dna(self):
        self.assertTrue(lists.validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag'))
        self.assertFalse(lists.validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag'))
        self.assertFalse(lists.validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag'))

    def test_read_column(self):
        text = """1,0.1,0.001
2,0.2,0.002
3,0.3,0.003
4,0.4,0.004
5,0.5,0.005
6,0.6,0.006"""

        # and now we pass the file name to the function which will read the column
        self.assertEqual(lists.read_column(text, 2), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

    def test_pythagorean_triples(self):
        self.assertEqual(lists.pythagorean_triples(10), [[3, 4, 5], [4, 3, 5]])


    
        
if __name__ == '__main__':
    unittest.main()