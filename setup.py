import os
from setuptools import setup


long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()


base_url = 'https://github.com/sendgrid/'
version = '3.1.0'
setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url='{}python-http-client'.format(base_url),
    download_url='{}python-http-client/tarball/{}'.format(base_url, version),
    packages=['python_http_client'],
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description=long_description,
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
        'Programming Language :: Python :: 3.7'
    ]
)
