import sys
import os
from setuptools import setup

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

def getRequires():
    deps = []
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
    return deps

base_url = 'https://github.com/sendgrid/'
version = '2.3.0'
setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url='{0}python-http-client'.format(base_url),
    download_url='{0}python-http-client/tarball/{1}'.format(base_url, version),
    packages=['python_http_client'],
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description=long_description,
    install_requires=getRequires(),
    keywords=[
        'REST',
        'HTTP',
        'API'],
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
