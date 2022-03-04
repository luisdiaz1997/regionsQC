from importlib_metadata import entry_points
from setuptools import setup, find_packages

setup(name='regionsQC', 
    version='0.1', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click', 'bioframe', 'cooler'],
    entry_points={
        'console_scripts': ['regionsQC = regionsQC.main:cli']

    },

    )