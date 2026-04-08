import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # --- Positive Cases ---

    def test_basic_addition(self):
        """Normal usage: 12 + 3 = 15"""
        self.calc.press_number("1")
        self.calc.press_number("2")
        self.calc.press_operator("+")
        self.calc.press_number("3")
        result = self.calc.evaluate()
        self.assertEqual(result, "15")

    def test_chained_operations(self):
        """Normal usage: 10 * 2 + 5 = 25 (chain via operator press)"""
        self.calc.press_number("1")
        self.calc.press_number("0")
        self.calc.press_operator("*")
        self.calc.press_number("2")
        self.calc.press_operator("+")  # should evaluate 10*2=20 and carry forward
        self.calc.press_number("5")
        result = self.calc.evaluate()
        self.assertEqual(result, "25")

    # --- Negative Cases ---

    def test_division_by_zero(self):
        """Invalid input: dividing by zero should return Error"""
        self.calc.press_number("9")
        self.calc.press_operator("/")
        self.calc.press_number("0")
        result = self.calc.evaluate()
        self.assertEqual(result, "Error")

    def test_input_blocked_after_error(self):
        """After an error, pressing numbers should not change the display"""
        self.calc.press_number("5")
        self.calc.press_operator("/")
        self.calc.press_number("0")
        self.calc.evaluate()
        result = self.calc.press_number("9")
        self.assertEqual(result, "Error")

    # --- Edge Cases ---

    def test_evaluate_with_no_input(self):
        """Edge case: pressing = with nothing entered should return empty string"""
        result = self.calc.evaluate()
        self.assertEqual(result, "")

    def test_operator_without_left_number(self):
        """Edge case: pressing operator before any number should do nothing"""
        result = self.calc.press_operator("+")
        self.assertEqual(result, "")

    def test_replacing_operator(self):
        """Edge case: pressing multiple operators in a row should only keep the last one"""
        self.calc.press_number("7")
        self.calc.press_operator("+")
        self.calc.press_operator("*")
        self.calc.press_operator("-")
        self.calc.press_number("3")
        result = self.calc.evaluate()
        self.assertEqual(result, "4")

    def test_clear_resets_state(self):
        """Edge case: clear mid-expression should fully reset"""
        self.calc.press_number("9")
        self.calc.press_operator("+")
        self.calc.press_number("1")
        self.calc.clear()
        result = self.calc.evaluate()
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
