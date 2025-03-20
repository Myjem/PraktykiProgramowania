import unittest
from fun import *

class testCase(unittest.TestCase):

    def testAddIsEmpty(self):
        self.assertEqual(Add(""),0)

    def testAddIsOne(self):
        self.assertEqual(Add("1"),1)

    def testAddSum(self):
        self.assertEqual(Add("1,2"),3)

    def testMultipleInputs(self):
        self.assertEqual(Add("1,2,3"),6)

    def testNewLine(self):
        self.assertEqual(Add("1\n2,3"),6)
        self.assertEqual(Add("1\n2,3"), 6)
        self.assertEqual(Add("1,\n2,3"), 6)
        self.assertEqual(Add("1,,\n2,3,"), 6)
        self.assertEqual(Add("1,,\n,,2,\n3,"), 6)

