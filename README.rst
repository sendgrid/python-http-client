.. image:: https://github.com/sendgrid/sendgrid-python/raw/HEAD/twilio_sendgrid_logo.png
   :target: https://www.sendgrid.com

|Test and Deploy Badge| |Twitter Follow| |Codecov branch| |Code Climate| |Python Versions| |PyPI Version| |GitHub contributors| |MIT licensed|

**Quickly and easily access any RESTful or RESTful-like API.**

If you are looking for the Twilio SendGrid API client library, please see `this repo`_.

Table of Contents
=================

-  `Installation <#installation>`__
-  `Quick Start <#quick-start>`__
-  `Usage <#usage>`__
-  `How to Contribute <#how-to-contribute>`__
-  `Local Setup of the Project <#local-setup-of-the-project>`__
-  `Troubleshooting <#troubleshooting>`__
-  `Announcements <#announcements>`__
-  `Thanks <#thanks>`__
-  `About <#about>`__
-  `License <#license>`__

Installation
============

Prerequisites
-------------

-  Python version 2.7 or 3.4+

Install Package
---------------

.. code:: bash

    pip install python_http_client

or

.. code:: bash

    easy_install python_http_client

API Key
-------

Store your Twilio SendGrid API key in a ``.env`` file.

.. code:: bash

    cp .env_sample .env

Edit the ``.env`` file and add your API key.

Quick Start
===========

Here is a quick example:

``GET /your/api/{param}/call``

.. code:: python

    import python_http_client

    global_headers = {"Authorization": "Bearer XXXXXXX"}
    client = Client(host='base_url', request_headers=global_headers)
    client.your.api._(param).call.get()
    print(response.status_code)
    print(response.headers)
    print(response.body)

``POST /your/api/{param}/call`` with headers, query parameters and a request body with versioning.

.. code:: python

    import python_http_client

    global_headers = {"Authorization": "Bearer XXXXXXX"}
    client = Client(host='base_url', request_headers=global_headers)
    query_params = {"hello":0, "world":1}
    request_headers = {"X-Test": "test"}
    data = {"some": 1, "awesome": 2, "data": 3}
    response = client.your.api._(param).call.post(request_body=data,
                                                  query_params=query_params,
                                                  request_headers=request_headers)
    print(response.status_code)
    print(response.headers)
    print(response.body)

Usage
=====

-  `Example Code`_

How to Contribute
=================

We encourage contribution to our projects, please see our `CONTRIBUTING`_ guide for details.

Quick links:

-  `Improvements to the Codebase`_
-  `Review Pull Requests`_

Local Setup of the Project
==========================

The simplest local development workflow is by using docker.

1. Install Docker
2. Run ``docker-compose build`` (this builds the container)
3. Run ``docker-compose up`` (this runs tests by default)

Troubleshooting
===============

Please see our `troubleshooting guide`_ for any issues.

Announcements
=============

All updates to this project is documented in our `CHANGELOG`_.

Thanks
======

We were inspired by the work done on `birdy`_ and `universalclient`_.

About
=====

**python-http-client** is maintained and funded by Twilio SendGrid, Inc.
The names and logos for **python-http-client** are trademarks of Twilio SendGrid, Inc.

License
=======

`The MIT License (MIT)`_

.. _this repo: https://github.com/sendgrid/sendgrid-python
.. _Example Code: https://github.com/sendgrid/python-http-client/tree/HEAD/examples
.. _CONTRIBUTING: https://github.com/sendgrid/python-http-client/blob/HEAD/CONTRIBUTING.md
.. _Improvements to the Codebase: https://github.com/sendgrid/python-http-client/blob/HEAD/CONTRIBUTING.md#improvements-to-the-codebase
.. _Review Pull Requests: https://github.com/sendgrid/python-http-client/blob/HEAD/CONTRIBUTING.md#code-reviews
.. _troubleshooting guide: https://github.com/sendgrid/python-http-client/blob/HEAD/TROUBLESHOOTING.md
.. _CHANGELOG: https://github.com/sendgrid/python-http-client/blob/HEAD/CHANGELOG.md
.. _birdy: https://github.com/inueni/birdy
.. _universalclient: https://github.com/dgreisen/universalclient
.. _The MIT License (MIT): https://github.com/sendgrid/python-http-client/blob/HEAD/LICENSE
.. _this is an incredible opportunity to join our #DX team: https://sendgrid.com/careers/role/1421152/?gh_jid=1421152

.. |Test and Deploy Badge| image:: https://github.com/sendgrid/python-http-client/actions/workflows/test-and-deploy.yml/badge.svg
   :target: https://github.com/sendgrid/python-http-client/actions/workflows/test-and-deploy.yml
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow
   :target: https://twitter.com/sendgrid
.. |Codecov branch| image:: https://img.shields.io/codecov/c/github/sendgrid/python-http-client/main.svg?style=flat-square&label=Codecov+Coverage
   :target: https://codecov.io/gh/sendgrid/python-http-client
.. |Code Climate| image:: https://codeclimate.com/github/sendgrid/python-http-client/badges/gpa.svg
   :target: https://codeclimate.com/github/sendgrid/python-http-client
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/python-http-client.svg
   :target: https://pypi.org/project/python-http-client
.. |PyPI Version| image:: https://img.shields.io/pypi/v/python-http-client.svg
   :target: https://pypi.org/project/python-http-client
.. |GitHub contributors| image:: https://img.shields.io/github/contributors/sendgrid/python-http-client.svg
   :target: https://github.com/sendgrid/python-http-client/graphs/contributors
.. |MIT licensed| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/sendgrid/python-http-client/blob/HEAD/LICENSE
