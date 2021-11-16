#!/usr/bin/env python3
import unittest
from main import rightorentation, straightorentation, leftorentation, rightofway

class Test_Rightofway(unittest.TestCase):
    def testrightorentation1_(self):
        ans = rightorentation("South")
        correct = "East"
        self.assertEqual(ans,correct)
    def testrightorentation2_(self):
        ans = rightorentation("East")
        correct = "North"
        self.assertEqual(ans,correct)
    def teststraightoreantation1_(self):
        ans = straightorentation("South")
        correct = "North"
        self.assertEqual(ans,correct)
    def teststraightoreantation2_(self):
        ans = straightorentation("East")
        correct = "West"
        self.assertEqual(ans,correct)
    def teststraihtoreantation3_(self):
        ans = straightorentation("North")
        correct = "South"
        self.assertEqual(ans,correct)
    def testleftoreantation1_(self):
        ans = leftorentation("North")
        correct = "East"
        self.assertEqual(ans,correct)
    def testleftoreantation2_(self):
        ans = leftorentation("East")
        correct = "South"
        self.assertEqual(ans,correct)
    def testrightofway1_(self):
        datalist = ["South","West","East"]
        ans = rightofway(datalist)
        correct = "Yes"
        self.assertEqual(ans,correct)
    def testrightofway2_(self):
        datalist = ["South","North","North"]
        ans = rightofway(datalist)
        correct = "No"
        self.assertEqual(ans,correct)
    def testrightofway3_(self):
        datalist = ["South","North","East"]
        ans = rightofway(datalist)
        correct = "Yes"
        self.assertEqual(ans,correct)
# 1) You want to pass straight through the 
# intersection; another vehicle is approaching 
# from your right.

# 2)You want to turn left at the intersection; 
# another vehicle is approaching from the opposite
# direction or from your right.
        
if __name__ == "__main__":
    unittest.main(verbosity=2)

