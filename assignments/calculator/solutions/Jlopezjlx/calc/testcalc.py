import unittest
import calc

class testing_calc(unittest.TestCase):
    
    
    def test_sumar(self):
        result = calc.sumar(2,3)
        self.assertEqual(5,result)
    

    def test_restar(self):
        result = calc.restar(2,3)
        expected = 2 - 3
        self.assertEqual(expected,result)
    

    def test_multiplcacion(self):
        result = calc.multiplicacion(2,3)
        expected = 2 * 3
        self.assertEqual(expected, result)
    

    def test_division(self):
        result = calc.division(2,3)
        expected = 2 / 3
        self.assertEqual(expected, result)  
    

    def test_restante(self):
        result = calc.restante(2,3)
        expected = 2 % 3
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()



