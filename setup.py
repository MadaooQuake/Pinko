import os
from setuptools import setup

# Utility function to read the README file.
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pinko",
    version = "1.0.0dev1",
    author = "Marcin Kielkowski",
    author_email = "kielkowskimarcin@prokonto.pl",
    description = ("Pinko is arcade game"),
    license = "BSD",
    keywords = "Pinko Game in Python",
    url = "https://github.com/MadaooQuake/Pinko",
    packages=['core', 'levels', 'main', 'tests*'],
    classifiers=[
        "Development Status :: 1.0.0dev1",
        "Topic ::  Game",
        "License :: OSI Approved :: BSD License",
    ],
)