#!/usr/bin/env python3
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

with open(path.join(here, 'yuid', 'version.txt')) as f:
    version = f.read().strip()

setup(
    name='yuid',
    description='youtube-like UUIDs',
    long_description=long_description,
    url='https://github.com/ogastorga/yuid',

    version=version,

    author='Og Astorga',
    author_email='og@ogastorga.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=[
        'uuid',
    ],

    packages=[
        'yuid',
    ],

    test_require=[
        'pytest'
    ]
)
