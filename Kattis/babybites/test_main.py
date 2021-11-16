#!/usr/bin/env python3
import unittest
from main import count_mumbles

class Test_Babybites(unittest.TestCase):
    def test1_(self):
        datalist = ['1','2','3','mumble','5']
        ans = count_mumbles(datalist,5)
        correct = True
        self.assertEqual(ans,correct)
    def test2_(self):
        datalist = ['1','2','mumble','mumble','5']
        ans = count_mumbles(datalist,5)
        correct = True
        self.assertEqual(ans,correct)
    def test3_(self):
        datalist = ['1','2','mumble','5','6']
        ans = count_mumbles(datalist,5)
        correct = False
        self.assertEqual(ans,correct)
    def test4_(self):
        datalist = ['1','2','mumble','5','6','mumble','mumble']
        ans = count_mumbles(datalist,8)
        correct = False
        self.assertEqual(ans,correct)
    
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

