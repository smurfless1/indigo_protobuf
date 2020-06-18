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
    packages=["indigo_protobuf", "indigo_protobuf_betterproto"],
    python_requires='>=3.7',
    install_requires=[
        'arrow',
        'betterproto',
        'grpcio',
        'protobuf',
        'python-dateutil',
    ],
    extras_require={
        'dev': [
            'betterproto[compiler]',
            'grpcio-tools',
            'invoke',
            'tox'
        ]
    },
)
