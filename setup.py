#!/usr/bin/env python
import sys
import os.path

from setuptools import setup, find_packages, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    extensions = [
        Extension(
            'simdjson',
            sources=[
                'simdjson.cpp'
            ],
            language='c++'
        )
    ]
else:
    extensions = cythonize([
        Extension(
            'simdjson',
            sources=[
                'simdjson.pyx'
            ],
            language='c++'
        )
    ], compiler_directives={
        'embedsignature': True
    })

root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('utf-8')


setup(
    name='pysimdjson',
    packages=find_packages(),
    version='1.2.1',
    description='simdjson bindings for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tyler Kennedy',
    author_email='tk@tkte.ch',
    url='http://github.com/TkTech/pysimdjson',
    keywords=['json', 'simdjson'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    tests_require=[
        'pytest>=2.10',
        'Cython',
        'm2r',
        'sphinx',
        'ghp-import',
        'bumpversion'
    ],
    ext_modules=extensions,
    package_data = {
        '': ['*.pyd']
    }
)
