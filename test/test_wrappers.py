from unittest import TestCase
import python_tools as pt


def _test_function(x, y, z):
    """Just a test function that doesn't do anything

    :param x: not relevant
    :param y: not relevant
    :param z: not relevant
    """
    return x + y + z


class Test(TestCase):
    def test__get_func_str(self):
        self.assertEqual('_test_function(x, y, z)', pt.wrappers._get_func_str(_test_function))

    def test_debug(self):
        pass  # todo

    def test_timer(self):
        pass  # todo
