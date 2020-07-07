# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='keskivonfer',
    version="1.01",
    packages=find_packages(),
    author="megadose",
    install_requires=["argparse","fake_useragent"],
    description="Keskivonfer is a tool that allows you to extract information from a vinted account",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/keskivonfer',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
