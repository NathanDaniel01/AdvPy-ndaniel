#!/usr/bin/env python3

import unittest

from main import distance, answer

PLACES = 6

class Test_Jointjogjam(unittest.TestCase):
    def test1_distance(self):
        ans = distance(0,0,1,1)
        correct = 1.41421356237
        self.assertAlmostEqual(ans,correct,PLACES)
    
    def test1_answer(self):
        initDist = distance(0,0,0,0)
        finalDist = distance(1,1,2,2)
        ans = answer(initDist,finalDist)
        correct = 1.41421356237
        self.assertAlmostEqual(ans,correct, PLACES)
if __name__ == "__main__":
    unittest.main(verbosity=2)

