from unittest import TestCase
import python_tools as pt

def _test_f_0():
    """Just a test function that doesn't do anything useful
    """
    pass


def _test_f_1(x):
    """Just a test function that doesn't do anything useful

    :return: x
    :param x: not relevant
    """
    return x


def _test_f_3(x, y, z):
    """Just a test function that doesn't do anything useful

    :return: sum of x, y, z
    :param x: not relevant
    :param y: not relevant
    :param z: not relevant
    """
    return x + y + z


class Test(TestCase):
    def test__get_func_str(self):
        self.assertEqual('_test_f_0()', pt.wrappers._get_func_str(_test_f_0))
        self.assertEqual('_test_f_1(x)', pt.wrappers._get_func_str(_test_f_1))
        self.assertEqual('_test_f_3(x, y, z)', pt.wrappers._get_func_str(_test_f_3))

    def test_debug(self):
        pass  # todo

    def test_timer(self):
        pass  # todo
