import os
import importlib.util
import itertools
import tempfile
import pytest

import pydollar
pydollar.install_import_hook()
from _tests import cases, my_evil_values, price
from _test_exclamation_mark import cases_excl, my_evil_excl, greeting_excl

def _test_case(case):
    assert case() == case.expected

@pytest.mark.parametrize('case', cases)
def test_cases(case):
    _test_case(case)

@pytest.mark.parametrize('case', cases_excl)
def test_exclamation_mark_cases(case):
    _test_case(case)

def test_sympy():
    from _tests_sympy import cases
    for case in cases:
        _test_case(case)

def test_evil_values():
    assert my_evil_values == ('_DOLLAR_SIGN_LITERAL_0_', '_DOLLAR_SIGN_LITERAL_1_')
    assert price == '$42'

def test_evil_values_exclamation_mark():
    assert my_evil_excl_values == ('_EXLAMATION_MARK_LITERAL_0_', '_EXLAMATION_MARK_LITERAL_1_')
    assert greeting_excl == 'hello world!'


if __name__ == '__main__':
    test_sympy()
    test_evil_values()
    test_evil_values_exclamation_mark()
    for case in itertools.chain(cases, cases_excl):
        _test_case(case)
