
# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-project-name',
    version='0.1.0',
    description='python-project-description',
    long_description=readme,
    author='Damien Murphy',
    author_email='damienomurchu@gmail.com',
    url='https://github.com/damienomurchu/py-proj',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
