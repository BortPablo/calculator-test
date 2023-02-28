import sys
import random
import unittest
# Import the class from '../src/medium_calculator.py'
sys.path.append('./src')
from medium_calculator import MediumCalculator

class TestMediumCalculator(unittest.TestCase):
    #random float between 1 and 100000

    def setUp(self) -> None:
        self.rdm = random.uniform(1, 1000)
        self.rdm2 = random.uniform(1, 1000)
        self.power = random.randint(2, 5)


    def test_init(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.tot, self.rdm)

    def test_add(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.add(self.rdm2), self.rdm + self.rdm2)
        
    def test_subtract(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.subtract(self.rdm2), self.rdm - self.rdm2)
        
    def test_multiply(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.multiply(self.rdm2), self.rdm * self.rdm2)
        
    def test_divide(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.divide(self.rdm2), self.rdm / self.rdm2)
        
    def test_power(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(calc.power(self.power), self.rdm ** self.power)
        
    def test_repr(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(repr(calc), str(self.rdm))
        
    def test_str(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertEqual(str(calc), str(self.rdm))
        
    def test_divide_by_zero(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertRaises(ZeroDivisionError, calc.divide, 0)
    
    def test_reset(self) -> None:
        calc = MediumCalculator(self.rdm)
        calc.reset()
        self.assertEqual(calc.tot, 0)
    
    def test_infinite(self) -> None:
        calc = MediumCalculator(self.rdm)
        self.assertRaises(OverflowError, calc.power, 1000000)
        
    def test_invalid_operation(self) -> None:
        calc = MediumCalculator(10.2)
        self.assertRaises(ValueError, calc.divide, "a")
        self.assertRaises(ValueError, calc.power, "a")
        self.assertRaises(ValueError, calc.add, "a")
        self.assertRaises(ValueError, calc.subtract, "a")
        self.assertRaises(ValueError, calc.multiply, "a")

if __name__ == "__main__":
    unittest.main()