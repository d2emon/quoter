#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of quoter.
# https://github.com/d2emon/quoter.git

# Licensed under the GPL-3.0 license:
# http://www.opensource.org/licenses/GPL-3.0-license
# Copyright (c) 2018, Dmitry Kutsenko <d2emonium@gmail.com>

from os import path
import sys

HERE = path.abspath(path.dirname(__file__))
PARENT_DIR = path.abspath(path.join(HERE, 'src'))
sys.path.append(PARENT_DIR)

from setuptools import setup, find_packages
# from cx_Freeze import setup, Executable
from quoter import __version__

# To use a consistent encoding
# from codecs import open

# tests_require = [
#     'mock',
#     'nose',
#     'coverage',
#     'yanc',
#     'preggy',
#     'tox',
#     'ipdb',
#     'coveralls',
#     'sphinx',
# ]

# Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

# with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
#     version = f.read().strip()

# with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
#     requirements = f.read().splitlines()

# build_exe_options = {
#     # "icon": r"assets/favicon/favicon.ico",
#     "includes": [
#         "config",
#         "sqlalchemy.sql.default_comparator",
#         "faker.providers",
#         "jinja2.ext",
#     ],
#     "include_files": [
#         "src/static",
#         "src/templates",
#         "db",
#         "imports",
#         "log",
#     ],
#     # "path": [
#     #     path.dirname(__file__),
#     # ],
# }

# base = None
setup(
    name='quoter',
    version=__version__,
    description='Random quote',
    # long_description=long_description,
    long_description='''
Random quote
''',
    keywords='quote random',

    # Author details
    author='Dmitry Kutsenko',
    author_email='d2emonium@gmail.com',

    url='https://github.com/d2emon/quoter.git',
    license='GPL-3.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3.0 License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],

    # package_dir={'': 'src'},
    # packages=find_packages('./src', exclude=['tests']),
    packages=find_packages(),
    include_package_data=True,
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # py_modules=[
    #     "app",
    #     "config",
    # ],
    # install_requires=requirements,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        # 'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'quoter=quoter.cli:main',
            # 'server=app:run',
        ],
    },

    # executables = [Executable(
    #     "src/run_server.py",
    #     base=base,
    #     icon=r"src/assets/favicon/favicon.ico",
    # )],

    # options = {
    #     "build_exe": build_exe_options,
    # },
)
