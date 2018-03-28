#!/usr/bin/env python

import os
from setuptools import setup, find_packages

setup(name='iotdeviceprovisioner',
      version='1.0',
      description='Configure AWS Account for provisioning AWS IoT devices to use iotbotocredentialprovider',
      author='Craig I. Hagan',
      author_email='hagan@cih.com',
      url='n/a',
      packages = find_packages(exclude=["test"]),
      setup_requires=["pytest-runner"],
      tests_require=["pytest", "pytest-runner"],
)
