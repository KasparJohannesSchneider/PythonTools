import re
import time
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
    time.sleep(0.25)  # test the timing function
    return x + y + z


class Test(TestCase):
    def test__get_func_str(self):
        self.assertEqual('_test_f_0()', pt.debug_tools._get_func_str(_test_f_0))
        self.assertEqual('_test_f_1(x)', pt.debug_tools._get_func_str(_test_f_1))
        self.assertEqual('_test_f_3(x, y, z)', pt.debug_tools._get_func_str(_test_f_3))

    def test_run_fct_get_stdout(self):
        self.assertEqual('Hello World!\n', pt.run_fct_get_stdout(print, 'Hello World!'))
        self.assertEqual('', pt.run_fct_get_stdout(str, 5))

    def test_debug(self):
        # Wrap function and get stdout
        w_t_function = pt.debug_tools.debug(_test_f_3)
        stdout_str_lines = pt.run_fct_get_stdout(w_t_function, 1, 2, 3).split('\n')

        self.assertEqual('--debug--debug--debug--debug--debug--debug--debug--debug--debug--debug--',
                         stdout_str_lines[1])
        self.assertEqual('--  Function: _test_f_3(x, y, z)',
                         stdout_str_lines[2])
        self.assertEqual('--  Arguments: (1, 2, 3)',
                         stdout_str_lines[3])
        self.assertEqual('--  Returned: 6',
                         stdout_str_lines[4])
        self.assertEqual('--  Time elapsed [ms]: ',
                         re.sub('\d+.\d+', '', stdout_str_lines[5]))
        self.assertAlmostEqual(0.25 * 1000,
                               float(re.search('\d+.\d+', stdout_str_lines[5])[0]), delta=50)
        self.assertEqual('--debug--debug--debug--debug--debug--debug--debug--debug--debug--debug--',
                         stdout_str_lines[6])

    def test_timer(self):
        # Wrap function and get stdout
        w_t_function = pt.debug_tools.timer(_test_f_3)
        stdout_str_lines = pt.run_fct_get_stdout(w_t_function, 1, 2, 3).split('\n')

        self.assertEqual('--timer--timer--timer--timer--timer--timer--timer--timer--timer--timer--',
                         stdout_str_lines[1])
        self.assertEqual('--  Function: _test_f_3(x, y, z)',
                         stdout_str_lines[2])
        self.assertEqual('--  Time elapsed [ms]: ',
                         re.sub('\d+.\d+', '', stdout_str_lines[3]))
        self.assertAlmostEqual(0.25 * 1000,
                               float(re.search('\d+.\d+', stdout_str_lines[3])[0]), delta=50)
        self.assertEqual('--timer--timer--timer--timer--timer--timer--timer--timer--timer--timer--',
                         stdout_str_lines[4])
