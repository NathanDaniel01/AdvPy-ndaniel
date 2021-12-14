#!/usr/bin/env python3
import unittest
from main import multiply, add


class Test_Buka(unittest.TestCase):
    def test1_Add(self):
        ans = add(1,8)
        correct = 9
        self.assertEqual(ans,correct)
    def test2_Add(self):
        ans = add(1000,100)
        correct = 1100
        self.assertEqual(ans,correct)
    def test3_Add(self):
        ans = add(1000000,3)
        correct = 1000003
        self.assertEqual(ans,correct)
    def test1_Multipy(self):
        ans = multiply(10,100)
        correct = 1000
        self.assertEqual(ans,correct)
    def test2_Multipy(self):
        ans = multiply(500,100)
        correct = 50000
        self.assertEqual(ans,correct)
    def test3_Multipy(self):
        ans = multiply(100,80)
        correct = 8000
        self.assertEqual(ans,correct)
   
    
if __name__ == "__main__":
    unittest.main(verbosity=2)

