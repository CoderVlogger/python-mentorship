import unittest
import app

class SimpleTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(app.plus(3, 2), 5)
        self.assertEqual(app.minus(3, 2), 1)
        self.assertEqual(app.multiply(3, 2), 6)
        self.assertEqual(app.div(4, 2), 2)

if __name__ == "__main__": 
    unittest.main()