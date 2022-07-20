import os
from setuptools import setup, find_packages


exec(open('iching/version.py').read())

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as rf:
    README = rf.read()

setup(
    name = 'miching',
    packages = find_packages(exclude=['test']),
    version = __version__,
    author = 'Bing D. Yee',
    author_email="bingdyee@gmail.com",
    url = "https://github.com/bingdyee/miching",
    license="Apache License 2.0",
    description = 'Any vital question you may have, ask it here.',
    long_description = README,
    keywords = 'Machine I-Ching, classification',
    python_requires = '>=3.6',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Public",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Application"
    ]
)

# run with: python setup.py bdist_wheel