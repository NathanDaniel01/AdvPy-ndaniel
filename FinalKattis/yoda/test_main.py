#!/usr/bin/env python3
import unittest
from main import Compare, printnumbers


class Test_Yoda(unittest.TestCase):
    def test1_Compare(self):
        arr1 = [4,5,6,7]
        arr2 = [1,2,3,4]
        ans = Compare(arr1,arr2)
        correct = [4,5,6,7]
        self.assertEqual(ans,correct)

    def test2_Compare(self):
        arr1 = [0,0,3]
        arr2 = [0,0,5]
        ans = Compare(arr1,arr2)
        correct = [0,0]
        self.assertEqual(ans,correct)

    def test3_Compare(self):
        arr1 = [4,2,6,7,9]
        arr2 = [3,3,6,4]
        ans = Compare(arr1,arr2)
        correct = [4,6,7,9]
        self.assertEqual(ans,correct)

    def test1_print(self):
        arr1 = [0,0]
        arr2 = [0,0,5]
        ans = printnumbers(arr1,arr2)
        correct = 0
        self.assertEqual(ans,correct)
        print(ans)
   
    def test2_print(self):
        arr1 = []
        arr2 = [8,7,6,5]
        ans = printnumbers(arr1,arr2)
        print(ans)
        correct = "1YODA"
        self.assertEqual(ans,correct)
    def test3_print(self):
        arr1 = [8,7,6,5]
        arr2 = []
        ans = printnumbers(arr1,arr2)
        print(ans)
        correct = "2YODA"
        self.assertEqual(ans,correct)


   
    
if __name__ == "__main__":
    unittest.main(verbosity=2)

