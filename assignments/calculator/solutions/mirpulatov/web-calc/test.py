import unittest
from calc import Calculator

calc = Calculator(6, 2)

class SimpleTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(calc.plus(), 8)
        self.assertEqual(calc.minus(), 4)
        self.assertEqual(calc.multiply(), 12)
        self.assertEqual(calc.div(), 3)

if __name__ == "__main__": 
    unittest.main()