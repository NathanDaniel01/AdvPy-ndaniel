#!/usr/bin/env python3
import unittest

from main import seperate, conversion


class Test_A_New_Alphabet(unittest.TestCase):
    def test1_Conversion(self):
        ans = conversion('i')
        correct = "|"
        self.assertEqual(ans,correct)

    def test2_Conversion(self):
        ans = conversion("o")
        correct = "0"
        self.assertEqual(ans,correct)

    def test3_Conversion(self):
        ans = seperate("a")
        correct = "@"
        self.assertEqual(ans,correct)
    def test1_Seperate(self):
        ans = seperate('can it be sepporated?')
        correct = "(@[]\[] |'][' 83 $3|D|D0|Z@']['3|)?"
        self.assertEqual(ans,correct)

    def test2_Seperate(self):
        ans = seperate("ALEX")
        correct = "@13}{"
        self.assertEqual(ans,correct)

    def test3_Seperate(self):
        ans = seperate("any numbers 5")
        correct = "@[]\[]`/ []\[]|_|[]\/[]83|Z$ 5"
        self.assertEqual(ans,correct)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)

