import unittest
import maths

class testing_calc(unittest.TestCase):
    
    
    def test_sumar(self):
        result = maths.sumar(2,3)
        self.assertEqual(5,result)
    

    def test_restar(self):
        result = maths.restar(2,3)
        expected = 2 - 3
        self.assertEqual(expected,result)
    

    def test_multiplcacion(self):
        result = maths.multiplicacion(2,3)
        expected = 2 * 3
        self.assertEqual(expected, result)
    

    def test_division(self):
        result = maths.division(2,3)
        expected = 2 / 3
        self.assertEqual(expected, result)  
    

    def test_restante(self):
        result = maths.restante(2,3)
        expected = 2 % 3
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()



