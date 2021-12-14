#!/usr/bin/env python3
import unittest
from main import getsqr,check

class Test_egypt(unittest.TestCase):
    def test1_getsqr(self):
        ans = getsqr(3)
        correct = 9
        self.assertEqual(ans,correct)
    def test2_getsqr(self):
        ans = getsqr(10)
        correct = 100
        self.assertEqual(ans,correct)
    def test3_getsqr(self):
        ans = getsqr(5)
        correct = 25
        self.assertEqual(ans,correct)
    def test1_check(self):
        ans = check(25,5)
        correct = "right"
        self.assertEqual(ans,correct)
    def test2_check(self):
        ans = check(3329,60)
        correct = "wrong"
        self.assertEqual(ans,correct)
    def test3_check(self):
        ans = check(9000000,3000)
        correct = "right"
        self.assertEqual(ans,correct)  
if __name__ == "__main__":
    unittest.main(verbosity=2)

