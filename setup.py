# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algorithm-design-manual-python',
    version='0.1.0',
    description='translation of C programs from Algorithm Design Manual(2nd edition) by Steven S. Skiena',
    long_description=readme,
    author='Chen Song',
    author_email='csong2022@berkeley.edu',
    url='https://github.com/csong2022/algorithm-design-manual-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

