import os
import importlib.util
import tempfile
import pytest

import pydollar
pydollar.install_import_hook()
from _tests import cases, my_evil_values, price


@pytest.mark.parametrize('case', cases)
def test_cases(case):
    assert case() == case.expected


def test_evil_values():
    assert my_evil_values == ('_DOLLAR_SIGN_LITERAL_0_', '_DOLLAR_SIGN_LITERAL_1_')
    assert price == '$42'
