import os
import sys
from setuptools import setup, find_packages


def getRequires():
    deps = []
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
    return deps

base_url = 'https://github.com/sendgrid/'
setup(
    name='python-http-client',
    version='1.0.0',
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url=base_url + 'python-http-client',
    packages=find_packages(),
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description='Check out the README at GitHub',
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)