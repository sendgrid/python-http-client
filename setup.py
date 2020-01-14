import io
import os
from distutils.file_util import copy_file
from setuptools import find_packages, setup


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()
version = io.open(os.path.join(dir_path, 'VERSION.txt'),
                  encoding='utf-8').read().strip()
base_url = 'https://github.com/sendgrid/'

copy_file(os.path.join(dir_path, 'VERSION.txt'),
          os.path.join(dir_path, 'python_http_client', 'VERSION.txt'),
          verbose=0)

setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url='{}python-http-client'.format(base_url),
    download_url='{}python-http-client/tarball/{}'.format(base_url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description_content_type='text/x-rst',
    long_description=readme,
    keywords=[
        'REST',
        'HTTP',
        'API'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
