#!/usr/bin/env python
from setuptools import setup

from distribute_setup import use_setuptools
from stratum import version

use_setuptools()

#python setup.py sdist upload


setup(
    name='stratum',
    version=version.VERSION,
    description='Stratum server implementation based on Twisted',
    author='slush',
    author_email='info@bitcion.cz',
    url='http://blog.bitcoin.cz/stratum',
    packages=[
        'stratum',
    ],
    py_modules=[
        'distribute_setup',
    ],
    zip_safe=False,
    install_requires=[
        'twisted',
        'ecdsa',
        'autobahn',
    ])
