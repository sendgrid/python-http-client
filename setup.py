import io
import os
import sys
from distutils.file_util import copy_file
from setuptools import find_packages, setup


def get_requires():
    deps = []
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()
version = io.open(os.path.join(dir_path, 'VERSION.txt'), encoding='utf-8').read().strip()
base_url = 'https://github.com/sendgrid/'

copy_file(os.path.join(dir_path, 'VERSION.txt'),
          os.path.join(dir_path, 'python_http_client', 'VERSION.txt'),
          verbose=0)

setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url='{0}python-http-client'.format(base_url),
    download_url='{0}python-http-client/tarball/{1}'.format(base_url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description=readme,
    install_requires=get_requires(),
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
