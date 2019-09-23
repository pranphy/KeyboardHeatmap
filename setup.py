#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 22:07

import setuptools

long_description = None

with open("README.md",'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="kbhmap",
    version="0.5.2",
    author="Prakash Gautam",
    author_email="info@pgautam.com.np",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'kbhmap':['images/*.png'],},
    #install_requres['numpy','scipy','matplotlib'],

    url='https://github.com/pranphy/KeyboardHeatmap',

    entry_points={
        'console_scripts':[
            'kbhmap=kbhmap:main',
        ],
    },


    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,

)

