![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

[![BuildStatus](https://travis-ci.org/sendgrid/python-http-client.svg?branch=master)](https://travis-ci.org/sendgrid/python-http-client)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/python)](https://dx.sendgrid.com/newsletter/python)
[![Twitter Follow](https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow)](https://twitter.com/sendgrid)
[![Codecov branch](https://img.shields.io/codecov/c/github/sendgrid/python-http-client/master.svg?style=flat-square&label=Codecov+Coverage)](https://codecov.io/gh/sendgrid/python-http-client)
[![Code Climate](https://codeclimate.com/github/sendgrid/python-http-client/badges/gpa.svg)](https://codeclimate.com/github/sendgrid/python-http-client)
[![GitHub contributors](https://img.shields.io/github/contributors/sendgrid/python-http-client.svg)](https://github.com/sendgrid/python-http-client/graphs/contributors)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)

**Quickly and easily access any RESTful or RESTful-like API.**

If you are looking for the SendGrid API client library, please see [this repo](https://github.com/sendgrid/sendgrid-python).

# Table of Contents

* [Installation](#installation)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [How to Contribute](#contribute)
* [Troubleshooting](#troubleshooting)
* [Announcements](#announcements)
* [Thanks](#thanks)
* [About](#about)
* [License](#license)

<a name="installation"></a>
# Installation

## Prerequisites

- Python version 2.6, 2.7, 3.4, 3.5 or 3.6

## Install Package

```bash
pip install python_http_client
```

or

```bash
easy_install python_http_client
```

<a name="quick-start"></a>
# Quick Start

Here is a quick example:

`GET /your/api/{param}/call`

```python
import python_http_client
global_headers = {"Authorization": "Basic XXXXXXX"}
client = Client(host='base_url', request_headers=global_headers)
client.your.api._(param).call.get()
print response.status_code
print response.headers
print response.body
```

`POST /your/api/{param}/call` with headers, query parameters and a request body with versioning.

```python
import python_http_client
global_headers = {"Authorization": "Basic XXXXXXX"}
client = Client(host='base_url', request_headers=global_headers)
query_params={"hello":0, "world":1}
request_headers={"X-Test": "test"}
data={"some": 1, "awesome": 2, "data": 3}
response = client.your.api._(param).call.post(request_body=data,
                                              query_params=query_params,
                                              request_headers=request_headers)
print response.status_code
print response.headers
print response.body
```

<a name="usage"></a>
# Usage

- [Example Code](https://github.com/sendgrid/python-http-client/tree/master/examples)

<a name="roadmap"></a>
# Roadmap

If you are interested in the future direction of this project, please take a look at our [milestones](https://github.com/sendgrid/python-http-client/milestones). We would love to hear your feedback.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our projects, please see our [CONTRIBUTING](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#feature-request)
- [Bug Reports](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#submit-a-bug-report)
- [Sign the CLA to Create a Pull Request](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#cla)
- [Improvements to the Codebase](https://github.com/sendgrid/python-http-client/blob/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/python-http-client/blob/master/TROUBLESHOOTING.md) for any issues.

<a name="announcements"></a>
# Announcements

All updates to this project is documented in our [CHANGELOG](https://github.com/sendgrid/python-http-client/blob/master/CHANGELOG.md).

<a name="thanks"></a>
# Thanks

We were inspired by the work done on [birdy](https://github.com/inueni/birdy) and [universalclient](https://github.com/dgreisen/universalclient).

<a name="about"></a>
# About

python-http-client is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

python-http-client is maintained and funded by SendGrid, Inc. The names and logos for python-http-client are trademarks of SendGrid, Inc.

<a name="license"></a>
# License

[The MIT License (MIT)](LICENSE.txt)
