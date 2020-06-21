import unittest
import math
import numpy as np

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import dictionaries

class TestDictionaries(unittest.TestCase):
    def test_create_dictionary(self):
        self.assertEqual(
            dictionaries.create_dict(
              ['Hamburg', 'Frankfurt', 'München'],
              [13, 11, 7]
            ),
            {'Hamburg': 13, 'Frankfurt': 11, 'München': 7}
        )


    def test_stock_value(self):
        stock = { "banana": 6, "apple": 0, "orange": 32, "pear": 15 }
        prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }

        self.assertEqual(dictionaries.stock_value(stock, prices), 6*4 + 32*1.5 + 15*3)


    def test_character_statistics(self):
        text = """
    To be, or not to be: that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles,
    And by opposing end them? To die: to sleep;
    No more; and by a sleep to say we end
    The heart-ache and the thousand natural shocks
    That flesh is heir to, 'tis a consummation
    Devoutly to be wish'd. To die, to sleep;
    To sleep: perchance to dream: ay, there's the rub;
    For in that sleep of death what dreams may come
    When we have shuffled off this mortal coil,
    Must give us pause: there's the respect
    That makes calamity of so long life;
    For who would bear the whips and scorns of time,
    The oppressor's wrong, the proud man's contumely,
    The pangs of despised love, the law's delay,
    The insolence of office and the spurns
    That patient merit of the unworthy takes,
    When he himself might his quietus make
    With a bare bodkin? who would fardels bear,
    To grunt and sweat under a weary life,
    But that the dread of something after death,
    The undiscover'd country from whose bourn
    No traveller returns, puzzzles the will
    And makes us rather bear those ills we have
    Than fly to others that we know not of?
    Thus conscience does make cowards of us all;
    And thus the native hue of resolution
    Is sicklied o'er with the pale cast of thought,
    And enterprises of great pith and moment
    With this regard their currents turn awry,
    And lose the name of action.--Soft you now!
    The fair Ophelia! Nymph, in thy orisons
    Be all my sins remember'd."""

        stats = dictionaries.character_statistics(text)

        self.assertEqual(stats, [
            ('e', 146),
            ('t', 120),
            ('o', 99),
            ('s', 88),
            ('a', 87),
            ('h', 79),
            ('r', 71),
            ('n', 70),
            ('i', 57),
            ('l', 44),
            ('d', 43),
            ('u', 41),
            ('f', 36),
            ('m', 32),
            ('w', 29),
            ('p', 24),
            ('c', 23),
            ('y', 18),
            ('b', 17),
            ('g', 14),
            ('k', 10),
            ('v', 8),
            ('z', 3),
            ('q', 2)
        ])

    
    
        
if __name__ == '__main__':
    unittest.main()