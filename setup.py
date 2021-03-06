from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('pulpcbcsol',
                         ['pulpcbc.pyx', 'CyEventHandler.cpp'],
                         libraries=['CbcSolver', 'Cbc', 'Cgl', 'Osi', 'OsiClp',
                                    'Clp', 'CoinUtils', 'rt', 'bz2', 'z',
                                    'blas', 'lapack'],
                         extra_compile_args=['-fpermissive'],
                         extra_link_args=['-Wl,--no-as-needed'],
                         language="c++",
                        )]

setup(
    name = 'pulpcbcsol',
    version = '0.1',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
)
