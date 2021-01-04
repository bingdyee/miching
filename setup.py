import os
from setuptools import setup, find_packages


exec(open('iching/version.py').read())

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as rf:
    README = rf.read()

setup(
    name = 'iching',
    packages = find_packages(exclude=['test']),
    version = __version__,
    author = 'Noa Swartz',
    author_email="fetaxyu@gmail.com",
    url = "https://github.com/vbintx/iching",
    license="Apache License 2.0",
    description = 'Any vital question you may have, ask it here.',
    long_description = README,
    keywords = 'I-Ching, classification',
    python_requires = '>=3.6',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Public",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Application"
    ]
)

# run with: python setup.py bdist_wheel