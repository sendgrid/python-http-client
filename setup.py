import io
import os

from distutils.file_util import copy_file
from setuptools import setup

dir_path = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(dir_path, 'README.rst')
version_path = os.path.join(dir_path, 'VERSION.txt')

with io.open(readme_path, encoding='utf-8') as readme_file:
    readme = readme_file.read()
with io.open(version_path, encoding='utf-8') as version_file:
    version = version_file.read().strip()

base_url = 'https://github.com/sendgrid/'

copy_file(version_path,
          os.path.join(dir_path, 'python_http_client', 'VERSION.txt'),
          verbose=0)

setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='help@twilio.com',
    url='{}python-http-client'.format(base_url),
    download_url='{}python-http-client/tarball/{}'.format(base_url, version),
    packages=['python_http_client'],
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
