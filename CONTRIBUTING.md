Hello! Thank you for choosing to help contribute to one of the Twilio SendGrid open source projects. There are many ways you can contribute and help is always welcome. We simply ask that you follow the following contribution policies.

**All third party contributors acknowledge that any contributions they provide will be made under the same open source license that the open source project is provided under.**

- [Feature Request](#feature-request)
- [Submit a Bug Report](#submit-a-bug-report)
    - [Please use our Bug Report Template](#please-use-our-bug-report-template)
- [Improvements to the Codebase](#improvements-to-the-codebase)
    - [Development Environment](#development-environment)
        - [Install and Run Locally](#install-and-run-locally)
            - [Prerequisites](#prerequisites)
            - [Initial setup:](#initial-setup)
            - [Execute:](#execute)
- [Understanding the Code Base](#understanding-the-code-base)
- [Testing](#testing)
- [Testing Multiple Versions of Python](#testing-multiple-versions-of-python)
    - [Prerequisites:](#prerequisites)
    - [Initial setup:](#initial-setup-1)
    - [Execute:](#execute-1)
- [Style Guidelines & Naming Conventions](#style-guidelines--naming-conventions)
- [Creating a Pull Request](#creating-a-pull-request)
- [Code Reviews](#code-reviews)

There are a few ways to contribute, which we'll enumerate below:

<a name="feature-request"></a>
## Feature Request

If you'd like to make a feature request, please read this section.

The GitHub issue tracker is the preferred channel for library feature requests, but please respect the following restrictions:

- Please **search for existing issues** in order to ensure we don't have duplicate bugs/feature requests.
- Please be respectful and considerate of others when commenting on issues

<a name="submit-a-bug-report"></a>
## Submit a Bug Report

Note: DO NOT include your credentials in ANY code examples, descriptions, or media you make public.

A software bug is a demonstrable issue in the code base. In order for us to diagnose the issue and respond as quickly as possible, please add as much detail as possible into your bug report.

Before you decide to create a new issue, please try the following:

1. Check the Github issues tab if the identified issue has already been reported, if so, please add a +1 to the existing post.
2. Update to the latest version of this code and check if the issue has already been fixed
3. Copy and fill in the Bug Report Template we have provided below

### Please use our Bug Report Template

In order to make the process easier, we've included a [sample bug report template](ISSUE_TEMPLATE.md).

<a name="improvements-to-the-codebase"></a>
## Improvements to the Codebase

We welcome direct contributions to the python-http-client code base. Thank you!

Please note that we utilize the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for Git to help keep project development organized and consistent.

### Development Environment ###

#### Install and Run Locally ####

##### Prerequisites #####

- Python 2.7 and 3.4+
- There are no external dependencies

##### Initial setup: #####

```bash
git clone https://github.com/sendgrid/python-http-client.git
cd python-http-client
```

##### Execute: #####

See the [examples folder](examples) to get started quickly.

<a name="understanding-the-codebase"></a>
## Understanding the Code Base

**/examples**

Working examples that demonstrate usage.

**/tests**

Unit and profiling tests.

**/python_http_client/client.py**

An HTTP client with a fluent interface using method chaining and reflection. By returning self on [__getattr__](python_http_client/client.py#L198), we can dynamically build the URL using method chaining and [__getattr__](python_http_client/client.py#L198) allows us to dynamically receive the method calls to achieve reflection.

This allows for the following mapping from a URL to a method chain:

`/api_client/{api_key_id}/version` maps to `client.api_client._(api_key_id).version.<method>()` where <method> is a [HTTP verb](python_http_client/client.py#L69).

**/python_http_client/config.py**

Loads the environment variables, if applicable.

<a name="testing"></a>
## Testing

All PRs require passing tests before the PR will be reviewed.

All test files are in the [`tests`](tests) directory.

For the purposes of contributing to this repo, please update the [`test_unit.py`](tests/test_unit.py) file with unit tests as you modify the code.

```bash
python -m unittest discover -v
```

<a name="testing-multiple-versions-of-python"></a>
## Testing Multiple Versions of Python

All PRs require passing tests before the PR will be reviewed.

### Prerequisites: ###

The above local "Initial setup" is complete

- [pyenv](https://github.com/yyuu/pyenv)
- [tox](https://pypi.python.org/pypi/tox)

### Initial setup: ###

Add `eval "$(pyenv init -)"` to your shell environment (.profile, .bashrc, etc) after installing tox, you only need to do this once.

```bash
pyenv install 2.7.11
pyenv install 3.4.3
pyenv install 3.5.2
pyenv install 3.6.0
python setup.py install
pyenv local 3.6.0 3.5.2 3.4.3 2.7.8
pyenv rehash
```

### Execute: ###

```bash
source venv/bin/activate
tox
```

<a name="style-guidelines-and-naming-conventions"></a>
## Style Guidelines & Naming Conventions

Generally, we follow the style guidelines as suggested by the official language. However, we ask that you conform to the styles that already exist in the library. If you wish to deviate, please explain your reasoning.

- [PEP8](https://www.python.org/dev/peps/pep-0008/)

Please run your code through:

- [pyflakes](https://pypi.python.org/pypi/pyflakes)
- [pylint](https://www.pylint.org/)
- [pep8](https://pypi.python.org/pypi/pep8)

<a name="creating-a-pull-request"></a>
## Creating a Pull Request

1. [Fork](https://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/sendgrid/python-http-client
   # Navigate to the newly cloned directory
   cd python-http-client
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/sendgrid/python-http-client
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout <dev-branch>
   git pull upstream <dev-branch>
   ```

3. Create a new topic branch off the `development` branch to

   contain your feature, change, or fix:

   ```bash
   git checkout development
   git checkout -b <topic-branch-name>
   ```

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely to be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4a. Create tests.

4b. Create or update the example code that demonstrates the functionality of this change to the code.

5. Locally merge (or rebase) the upstream `development` branch into your topic branch:

   ```bash
   git pull [--rebase] upstream development
   ```

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

7. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description against the `development` branch. All tests must be passing before we will review the PR.

<a name="code-reviews"></a>
## Code Reviews
If you can, please look at open PRs and review them. Give feedback and help us merge these PRs much faster! If you don't know how, GitHub has some great [information on how to review a Pull Request](https://help.github.com/articles/about-pull-request-reviews/).
