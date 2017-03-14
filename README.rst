pydollar
========

.. image:: http://hera.physchem.kth.se:9090/api/badges/bjodah/pydollar/status.svg
   :target: http://hera.physchem.kth.se:9090/bjodah/pydollar
   :alt: Build status
.. image:: https://img.shields.io/pypi/v/pydollar.svg
   :target: https://pypi.python.org/pypi/pydollar
   :alt: PyPI version
.. image:: https://img.shields.io/badge/python-3.5,3.6-blue.svg
   :target: https://www.python.org/
   :alt: Python version
.. image:: https://zenodo.org/badge/8840/bjodah/pydollar.svg
   :target: https://zenodo.org/badge/latestdoi/8840/bjodah/pydollar
.. image:: https://img.shields.io/pypi/l/pydollar.svg
   :target: https://github.com/bjodah/pydollar/blob/master/LICENSE
   :alt: License
.. image:: http://img.shields.io/badge/benchmarked%20by-asv-green.svg?style=flat
   :target: http://hera.physchem.kth.se/~pydollar/benchmarks
   :alt: airspeedvelocity
.. image:: http://hera.physchem.kth.se/~pydollar/branches/master/htmlcov/coverage.svg
   :target: http://hera.physchem.kth.se/~pydollar/branches/master/htmlcov
   :alt: coverage


.. contents::


About pydollar
--------------
`pydollar <https://github.com/bjodah/pydollar>`_ is a `Python <https://www.python.org>`_ module
which enables a non-native syntax for the dollar sign ``$`` in Python code. It allows you to
follow the DRY-principle (don't repeat yourself) more stricly when writing python code:

Take for example a file called ``mymodule.py``:

.. code:: python

   def my_func():
       hello, world = map(str.capitalize, $)
       print(hello, world)

we could then import from it by first intalling an import hook:

.. code:: python

   >>> import pydollar
   >>> pydollar.install_import_hook()
   >>> from mymodule import my_func
   >>> my_func()
   ('Hello', 'World')

    
Motivation
----------
f-strings were a great additon to Python 3.6, the ``$`` syntax follows it in spirit,
it simply allows you to write succinct code.

If ``$`` syntax (or more importantly, the functionality it provides) becomes official syntax
there would be a real-world benefit to widely used codebases, e.g. SymPy:

https://github.com/sympy/sympy/blob/sympy-1.0/sympy/core/symbol.py#L587


Installation
------------
Simplest way to install pydollar is to use ``pip``::
  
   $ python -m pip install --user pydollar

you can skip the ``--user`` flag if you have got root permissions.


Examples
--------
See the test files under `tests/ <https://github.com/bjodah/pydollar/tree/master/tests>`_.


License
-------
The source code is Open Source and is released under the very permissive
`"simplified (2-clause) BSD license" <https://opensource.org/licenses/BSD-2-Clause>`_.
See `LICENSE <LICENSE>`_ for further details.


Contributing
------------
Contributors are welcome to suggest improvements at https://github.com/bjodah/pydollar


Author
------
Björn I. Dahlgren, contact:
 - gmail address: bjodah
 - kth.se address: bda
