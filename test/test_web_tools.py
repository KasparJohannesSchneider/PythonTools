__all__ = ['Test']

from unittest import TestCase
import python_tools as pt


class Test(TestCase):
    def test_is_page_up(self):
        self.assertTrue(pt.is_page_up('https://www.twitter.com/'))
        self.assertFalse(pt.is_page_up('https://www.a1s2d3e5f2c5e4d2f5r1e23c5e1.com/'))
