import sys
import unittest
# Import the class from '../src/simple_calculator.py'
sys.path.append('./src')
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(calc.add(), 17.2)
        
    def test_subtract(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(round(calc.subtract(), 1), 3.2)
        
    def test_multiply(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(round(calc.multiply(),1), 71.4)
        
    def test_divide(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(calc.divide(), 1.457142857142857)
        
    def test_repr(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(repr(calc), "SimpleCalculator(10.2, 7)")
        
    def test_str(self) -> None:
        calc = SimpleCalculator(10.2, 7)
        self.assertEqual(str(calc), "SimpleCalculator(10.2, 7)")
        
    def test_divide_by_zero(self) -> None:
        calc = SimpleCalculator(10.2, 0)
        self.assertRaises(ZeroDivisionError, calc.divide)

if __name__ == "__main__":
    unittest.main()