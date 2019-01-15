from distutils.core import setup

from Cython.Build import cythonize

setup(name='little a',
      ext_modules=cythonize("a_traveller.pyx"))

# >> python setup.py build_ext --inplace
