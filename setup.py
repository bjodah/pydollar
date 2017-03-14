import io
import os
import warnings
from setuptools import setup
from pydollar import __version__

mod_name = 'pydollar'

def _path_under_setup(*args):
    return os.path.join(os.path.dirname(__file__), *args)

with io.open('%s.py' % mod_name, 'rt', encoding='utf-8') as f:
    short_description = f.read().split('"""')[1].split('\n')[1]
if not 10 < len(short_description) < 255:
    warnings.warn("Short description proably not read correctly")
long_descr = io.open(_path_under_setup('README.rst'), encoding='utf-8').read()
if not len(long_descr) > 100:
    warnings.warn("Long description from README.rst probably not read correctly.")
_author, _author_email = open(_path_under_setup('AUTHORS'), 'rt').readline().split('<')

setup_kwargs = dict(
    name=mod_name,
    py_modules=[mod_name],
    version=__version__,
    description=short_description,
    long_description=long_descr,
    author=_author.strip(),
    author_email=_author_email.split('>')[0].strip(),
    license='BSD',
    url='https://github.com/bjodah/pydollar',
)

if __name__ == '__main__':
    setup(**setup_kwargs)
