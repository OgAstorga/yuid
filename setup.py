#!/usr/bin/env python3
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(path.join(here, 'yuid', 'version.txt')) as f:
    version = f.read().strip()

setup(
    name='yuid',
    version=version,
    author='Og Astorga',
    author_email='og@ogastorga.com',
    description='youtube-like UUIDs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ogastorga/yuid',

    packages=[
        'yuid',
    ],

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],

    keywords=[
        'uuid',
    ],

    test_require=[
        'pytest'
    ]
)
