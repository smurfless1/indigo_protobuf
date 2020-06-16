#!/usr/bin/env python

from setuptools import setup


setup(
    name='indigo-protobuf',
    author='business@smurfless.com',
    url='',
    versioning='dev',
    setup_requires=['setupmeta'],
    dependency_links=['https://pypi.org/project/setupmeta'],
    # include_package_data=True,
    packages=["indigo_protobuf"],
    python_requires='>=3.7',
    install_requires=[
        'betterproto',
    ],
    extras_require={
        'dev': [
            'betterproto[compiler]',
            'invoke',
            'tox'
        ]
    },
)
