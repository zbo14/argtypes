"""
argtypes: a decorator to check argument types.
"""

from setuptools import setup, find_packages

setup(
    name='argtypes',
    version='0.1.0',
    author='Zachary Balder',
    license='Unlicense',
    py_modules=['argtypes'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(exclude=[]),
)