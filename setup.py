# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages
import time


_version = "0.1.dev%s" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "Python tool to find and list requirements of a Python project"


setup(
    name='requirements-detector',
    url='https://github.com/landscapeio/requirements-detector',
    author='landscape.io',
    author_email='code@landscape.io',
    description=_short_description,
    version=_version,
    scripts=['bin/detect-requirements'],
    install_requires=['astroid'],
    packages=_packages,
    license='MIT',
    keywords=('python requirements detector',)
)
