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
        """Edge case: pressing = with nothing entered should return 0"""
        result = self.calc.evaluate()
        self.assertEqual(result, "0")

    def test_operator_without_left_number(self):
        """Edge case: pressing operator before any number defaults left to 0"""
        result = self.calc.press_operator("+")
        self.assertEqual(result, "0+")

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
        """Edge case: clear mid-expression should fully reset to 0"""
        self.calc.press_number("9")
        self.calc.press_operator("+")
        self.calc.press_number("1")
        self.calc.clear()
        result = self.calc.evaluate()
        self.assertEqual(result, "0")

    # --- Decimal Cases ---

    def test_decimal_addition(self):
        """Positive: 1.5 + 2.5 = 4"""
        self.calc.press_number("1")
        self.calc.press_decimal()
        self.calc.press_number("5")
        self.calc.press_operator("+")
        self.calc.press_number("2")
        self.calc.press_decimal()
        self.calc.press_number("5")
        result = self.calc.evaluate()
        self.assertEqual(result, "4")

    def test_decimal_less_than_one(self):
        """Positive: pressing . first gives 0. prefix, so .5 + .3 = 0.8"""
        self.calc.press_decimal()
        self.calc.press_number("5")
        self.calc.press_operator("+")
        self.calc.press_decimal()
        self.calc.press_number("3")
        result = self.calc.evaluate()
        self.assertEqual(result, "0.8")

    def test_duplicate_decimal_ignored(self):
        """Edge case: pressing . twice on the same number should be ignored"""
        self.calc.press_number("1")
        self.calc.press_decimal()
        self.calc.press_decimal()
        self.calc.press_number("5")
        result = self.calc.press_number("0")
        self.assertEqual(result, "1.50")

    def test_decimal_after_operator(self):
        """Edge case: pressing . right after an operator starts right operand as 0."""
        self.calc.press_number("2")
        self.calc.press_operator("*")
        self.calc.press_decimal()
        self.calc.press_number("4")
        result = self.calc.evaluate()
        self.assertEqual(result, "0.8")

    def test_clear_after_error_resets_to_zero(self):
        """Positive: after error, clear should reset display to 0"""
        self.calc.press_number("1")
        self.calc.press_operator("/")
        self.calc.press_number("0")
        self.calc.evaluate()
        result = self.calc.clear()
        self.assertEqual(result, "0")
        self.assertFalse(self.calc.is_error())

    def test_number_press_after_error_clears_and_inputs(self):
        """Positive: after manually clearing error, pressing a number starts fresh"""
        self.calc.press_number("5")
        self.calc.press_operator("/")
        self.calc.press_number("0")
        self.calc.evaluate()
        self.calc.clear()
        result = self.calc.press_number("7")
        self.assertEqual(result, "7")


if __name__ == "__main__":
    unittest.main()
