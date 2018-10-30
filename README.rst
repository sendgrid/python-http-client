.. image:: https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png
   :target: https://www.sendgrid.com

|Build Status| |Email Notifications Badge| |Twitter Follow| |Codecov branch| |Code Climate| |Python Versions| |PyPI Version| |GitHub contributors| |MIT licensed|

**Quickly and easily access any RESTful or RESTful-like API.**

If you are looking for the SendGrid API client library, please see `this repo`_.

Table of Contents
=================

-  `Installation <#installation>`__
-  `Quick Start <#quick-start>`__
-  `Usage <#usage>`__
-  `Roadmap <#roadmap>`__
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

Store your SendGrid API key in a ``.env`` file.

.. code:: bash

    cp .env_sample .env

Edit the ``.env`` file and add your API key.

Quick Start
===========

Here is a quick example:

``GET /your/api/{param}/call``

.. code:: python

    import python_http_client

    global_headers = {"Authorization": "Basic XXXXXXX"}
    client = Client(host='base_url', request_headers=global_headers)
    client.your.api._(param).call.get()
    print(response.status_code)
    print(response.headers)
    print(response.body)

``POST /your/api/{param}/call`` with headers, query parameters and a request body with versioning.

.. code:: python

    import python_http_client

    global_headers = {"Authorization": "Basic XXXXXXX"}
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

Roadmap
=======

If you are interested in the future direction of this project, please take a look at our `milestones`_.
We would love to hear your feedback.

How to Contribute
=================

We encourage contribution to our projects, please see our `CONTRIBUTING`_ guide for details.

Quick links:

-  `Feature Request`_
-  `Bug Reports`_
-  `Sign the CLA to Create a Pull Request`_
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

PRODUCT • IRVINE
Developer Experience Engineer
As a Developer Experience Engineer at SendGrid, you will write high-quality, customer-friendly 
code to help developers embed SendGrid’s marketing and transactional email functionality in 
their applications.  In addition, you will be on the lookout to identify the features they need, and to 
help the community to contribute their experience. You will be a key contributor to and maintainer 
of our open source libraries and our process for providing World Class Developer Experience to 
our community.

What You’ll Do
* Work in the customer’s best interest, always
* Work closely with our current Developer Experience Engineering team and product manager, 
support team, Learning Experience team, and others in the company
* Maintain and improve the open source helper libraries/SDKs and sample code
* Help make SendGrid’s libraries and community the best on the internet
* Create new functionality, merge customer contributions, and build automations to improve the 
current process
* Love solving problems big or small in order to make the customer’s life easier
* Live by and champion our cultural values of Happy, Hungry, Honest, and Humble
About You
* A love for making customers’ lives better
* Desire to write high quality code that will scale well, be shared with the public, and scrutinized 
by the community
* Polyglot programmer: comfortable in several popular programming languages including Ruby, 
Node, Go, PHP, Python, C#, Java
* Well-versed in test-driven development and troubleshooting your own code
* Strong experience with API integrations
* Hands-on knowledge of Swagger/OpenAPI Spec
* Experience with GitHub and open source communities in general
* An appreciation for being part of a fast-paced environment
* Fastidious attention to consistency and accuracy
* Strong communication skills, ability to express technical concepts in verbal and written form 
as needed
* Ability to work in and across geographically distributed teams, build relationships, and 
integrate your workflow into theirs
* Bachelor's degree in CS or related equivalent experience required
About SendGrid
Founded in 2009, SendGrid built its reputation solving a key pain point of delivering transactional 
emails that respond to customer behavior (purchase receipts, order confirmations, password 
resets, etc.). In 2015, SendGrid expanded the platform into marketing email use cases, enabling 
customers to have one platform for both transactional and marketing email. We deliver over 45 
billion emails a month for customers like Airbnb, Spotify, and Yelp.



Thanks
======

We were inspired by the work done on `birdy`_ and `universalclient`_.

About
=====

**python-http-client** is guided and supported by the SendGrid `Developer Experience Team`_.

**python-http-client** is maintained and funded by SendGrid, Inc.
The names and logos for **python-http-client** are trademarks of SendGrid, Inc.

License
=======

`The MIT License (MIT)`_

.. _this repo: https://github.com/sendgrid/sendgrid-python
.. _Example Code: https://github.com/sendgrid/python-http-client/tree/master/examples
.. _milestones: https://github.com/sendgrid/python-http-client/milestones
.. _CONTRIBUTING: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md
.. _Feature Request: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#feature-request
.. _Bug Reports: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#submit-a-bug-report
.. _Sign the CLA to Create a Pull Request: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#cla
.. _Improvements to the Codebase: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#improvements-to-the-codebase
.. _Review Pull Requests: https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#code-reviews
.. _troubleshooting guide: https://github.com/sendgrid/python-http-client/blob/master/TROUBLESHOOTING.md
.. _CHANGELOG: https://github.com/sendgrid/python-http-client/blob/master/CHANGELOG.md
.. _birdy: https://github.com/inueni/birdy
.. _universalclient: https://github.com/dgreisen/universalclient
.. _Developer Experience Team: mailto:dx@sendgrid.com
.. _The MIT License (MIT): https://github.com/sendgrid/python-http-client/blob/master/LICENSE.txt

.. |Build Status| image:: https://travis-ci.org/sendgrid/python-http-client.svg?branch=master
   :target: https://travis-ci.org/sendgrid/python-http-client
.. |Email Notifications Badge| image:: https://dx.sendgrid.com/badge/python
   :target: https://dx.sendgrid.com/newsletter/python
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow
   :target: https://twitter.com/sendgrid
.. |Codecov branch| image:: https://img.shields.io/codecov/c/github/sendgrid/python-http-client/master.svg?style=flat-square&label=Codecov+Coverage
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
   :target: https://github.com/sendgrid/python-http-client/blob/master/LICENSE.txt
