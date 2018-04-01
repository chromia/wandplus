#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
import os

readme = ''
if os.path.exists('README.md'):
    readme = open('README.md').read()

setup(
    name='wandplus',
    version='0.1.0',
    description='Supplement library for Wand',
    long_description=readme,
    author='chromia',
    author_email='chromia@outlook.jp',
    url='https://github.com/chromia/wandplus',
    license='MIT',
    install_requires=['wand'],
    packages=find_packages(exclude=('tests', 'docs'))
)
