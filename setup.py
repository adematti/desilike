import os
import sys
from setuptools import setup


package_basename = 'desilike'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), package_basename))
import _version
version = _version.__version__


setup(name=package_basename,
      version=version,
      author='adematti',
      author_email='',
      description='Package for cosmological constraints',
      license='BSD3',
      url='http://github.com/adematti/desilike',
      install_requires=['numpy', 'scipy'],
      extras_require={},
      packages=[package_basename])
