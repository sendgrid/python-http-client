import sys
from setuptools import setup


def getRequires():
    deps = []
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
    return deps

base_url = 'https://github.com/sendgrid/'
version = '1.1.1'
setup(
    name='python_http_client',
    version=version,
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url=base_url + 'python-http-client',
    download_url=base_url + 'python-http-client' + "/tarball/" + version,
    packages=['python_http_client'],
    license='MIT',
    description='HTTP REST client, simplified for Python',
    long_description='Check out the README at GitHub',
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
        'Programming Language :: Python :: 3.5'
    ]
)
