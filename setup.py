#!/usr/bin/env python

from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'Readme.md')) as f:
    long_description = f.read()

setup(name='neuraltalk',
      version='1.0',
      description='NeuralTalk',
      long_description=long_description,
      license='BSD',
      url='https://github.com/Thanabhat/neuraltalk',
      packages=['neuraltalk', 'neuraltalk.imagernn'],
      data_files=[('neuraltalk', ['neuraltalk/data/README.md', 'neuraltalk/python_features/README.md', 'neuraltalk/python_features/deploy_features.prototxt'])]
     )
