import os
import importlib.util
import tempfile
import pytest

import pydollar
pydollar.install_import_hook()
from _tests import cases, my_evil_values, price

def _test_case(case):
    assert case() == case.expected

@pytest.mark.parametrize('case', cases)
def test_cases(case):
    _test_case(case)


def test_sympy():
    from _tests_sympy import cases
    for case in cases:
        _test_case(case)


def test_evil_values():
    assert my_evil_values == ('_DOLLAR_SIGN_LITERAL_0_', '_DOLLAR_SIGN_LITERAL_1_')
    assert price == '$42'


if __name__ == '__main__':
    test_sympy()
    test_evil_values()
    for case in cases:
        _test_case(case)
