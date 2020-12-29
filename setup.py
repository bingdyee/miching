# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


exec(open('iching/version.py').read())

setup(
    name = 'iching',
    description = 'Any vital question you may have, ask it here.',
    packages = find_packages(exclude=['test']),
    version = __version__,
    author = 'Noa Swartz',
    author_email="fetaxyu@gmail.com",
    url = "https://github.com/vbintx/iching",
    license="Apache License 2.0",
    python_requires = '>=3.6',
)

# run with: python setup.py bdist_wheel