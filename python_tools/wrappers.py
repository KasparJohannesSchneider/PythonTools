import time
import inspect


def debug(f):
    """
    Wrapper that prints function call, arguments, return value and the time elapsed.
    How to use: @wrappers.debug

    :param f: The function to be wrapped
    :return: The wrapped function
    """

    def wrapper(*args):
        t_start = time.time()
        val = f(*args)
        t_end = time.time()
        print('')
        print('--debug--debug--debug--debug--debug--debug--debug--debug--debug--debug--')
        print('--  Function: ' + _get_func_str(f))
        print('--  Arguments: ' + str(args))
        print('--  Returned: ' + str(val))
        print('--  Time elapsed [s]: ' + str((t_end - t_start) / 1000))
        print('--debug--debug--debug--debug--debug--debug--debug--debug--debug--debug--')
        print('')
        return val
    return wrapper


def timer(f):
    """
    Wrapper that times a function.
    How to use: @wrappers.timer

    :param f: The function to be wrapped
    :return: The wrapped function
    """

    def wrapper(*args):
        t_start = time.time()
        val = f(*args)
        t_end = time.time()
        print('')
        print('--timer--timer--timer--timer--timer--timer--timer--timer--timer--timer--')
        print('--  Function: ' + _get_func_str(f))
        print('--  Time elapsed [s]: ' + str((t_end - t_start) / 1000))
        print('--timer--timer--timer--timer--timer--timer--timer--timer--timer--timer--')
        print('')
        return val
    return wrapper


def _get_func_str(f):
    """
    Returns the name of a function including the argument names.

    :param f: The function of which the name should be returned
    :return: The name of the function f
    """
    f_name = str(f).split(' ')[1]
    f_args = str(inspect.getfullargspec(f).args) \
        .replace('[', '(') \
        .replace(']', ')') \
        .replace('\'', '')
    return f_name + f_args
