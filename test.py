import unittest
import calculator1

class TestCalculator(unittest.TestCase):

    def test_square_root(self):   
        self.assertAlmostEqual(calculator1.square_root(25), 5.0)    
        self.assertAlmostEqual(calculator1.square_root(9), 3.0) 
        self.assertAlmostEqual(calculator1.square_root(16), 4.0) 

    def test_factorial(self):     
        self.assertEqual(calculator1.factorial(5), 120)   
        self.assertEqual(calculator1.factorial(6), 720)   

    def test_natural_log(self):
        self.assertAlmostEqual(calculator1.natural_log(1), 0.0)           
        self.assertAlmostEqual(calculator1.natural_log(5), 1.6094379124) 

    def test_power(self):
        self.assertAlmostEqual(calculator1.power(2, 3), 8.0)        
        self.assertAlmostEqual(calculator1.power(4, 3), 64.0)    

if __name__ == '__main__':
    unittest.main()
