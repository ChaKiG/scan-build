#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='scan-build-ftt',
    version='2.0.2',
    author='László Nagy',
    author_email='rizsotto@gmail.com',
    url='https://github.com/rizsotto/scan-build',
    description='scan-build functional test tools.',
    zip_safe=False,
    packages=['tools'],
    entry_points={
        'console_scripts': [
            'cdb_diff = tools.diff:main',
            'cdb_expect = tools.expect:main'
        ]
    }
)
