from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['some_PYPI_package>=1.0']

setup(
    name='trainer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='My training application.'
)
