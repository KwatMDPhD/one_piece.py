"""
Computational Cancer Analysis Library v0.1


Authors:
Pablo Tamayo
pablo.tamayo.r@gmail.com
Computational Cancer Analysis, UCSD Cancer Center

Huwate (Kwat) Yeerna (Medetgul-Ernar)
kwat.medetgul.ernar@gmail.com
Computational Cancer Analysis, UCSD Cancer Center

James Jensen
jdjensen@eng.ucsd.edu
Laboratory of Jill Mesirov


Description:
Check dependencies and install missing ones.
"""
import pip
import random

from .support import _print

print('=' * 79)
print('=' * 20 + ' Computational Cancer Analysis Library ' + '=' * 20)
print('=' * 79)

_print('Checking dependencies ...')
packages_installed = [pkg.key for pkg in pip.get_installed_distributions()]
packages_needed = ['rpy2', 'numpy', 'pandas', 'scipy', 'scikit-learn', 'matplotlib', 'seaborn']
for pkg in packages_needed:
    if pkg not in packages_installed:
        _print('{} not found! Installing ...'.format(pkg))
        pip.main(['install', pkg])
_print('Using the following packages:')
for pkg in pip.get_installed_distributions():
    if pkg.key in packages_needed:
        _print('\t{} (v{})'.format(pkg.key, pkg.version))

SEED = 20121020
random.seed(SEED)

from . import support
from . import visualize
from . import information
from . import analyze

