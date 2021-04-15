__all__ = ['Test']

from unittest import TestCase
import python_tools as pt


class Test(TestCase):
    def test_sum_1_n(self):
        # Check return type
        self.assertEqual(int, type(pt.sum_1_n(1)))

        # Check math
        self.assertEqual(0, pt.sum_1_n(0))
        self.assertEqual(1, pt.sum_1_n(1))
        self.assertEqual(6, pt.sum_1_n(3))
        self.assertEqual(5050, pt.sum_1_n(100))

        # Test exceptions
        with self.assertRaises(AssertionError):
            pt.sum_1_n(-1)

    def test_ltm(self):
        self.assertEqual(1, pt.ltm(1))
        self.assertEqual(1, pt.ltm(2))
        self.assertEqual(3, pt.ltm(3))
        self.assertEqual(3, pt.ltm(4))
        self.assertEqual(3, pt.ltm(5))
        self.assertEqual(6, pt.ltm(6))
        self.assertEqual(6, pt.ltm(7))
        self.assertEqual(10, pt.ltm(13))
        self.assertEqual(10, pt.ltm(14))
        self.assertEqual(15, pt.ltm(15))
        self.assertEqual(5050, pt.ltm(5050))
        self.assertEqual(5050, pt.ltm(5051))

        # Test exceptions
        with self.assertRaises(AssertionError):
            pt.ltm(0)
            pt.ltm(-1)

    def test_is_triangular(self):
        # Test for cases that are triangular
        self.assertEqual(True, pt.is_triangular(1))
        self.assertEqual(True, pt.is_triangular(3))
        self.assertEqual(True, pt.is_triangular(5050))

        # Test for cases that aren't triangular
        self.assertEqual(False, pt.is_triangular(0))
        self.assertEqual(False, pt.is_triangular(-1))
        self.assertEqual(False, pt.is_triangular(5))
        self.assertEqual(False, pt.is_triangular(7))
        self.assertEqual(False, pt.is_triangular(200))
        self.assertEqual(False, pt.is_triangular(5049))
        self.assertEqual(False, pt.is_triangular(5051))
