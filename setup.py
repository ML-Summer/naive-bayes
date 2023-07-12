#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="naive-bayes",
      version="0.1.0",
      description="naive bayes classifier",
      author="ML Summer",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="",
      install_requires=["numpy==1.17.3",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        ],
      )