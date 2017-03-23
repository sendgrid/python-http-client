Hello! Thank you for choosing to help contribute to one of the SendGrid open source projects. There are many ways you can contribute and help is always welcome.  We simply ask that you follow the following contribution policies.

- [CLAs and CCLAs](#cla)
- [Roadmap & Milestones](#roadmap)
- [Feature Request](#feature_request)
- [Submit a Bug Report](#submit_a_bug_report)
- [Improvements to the Codebase](#improvements_to_the_codebase)
- [Understanding the Code Base](#understanding_the_codebase)
- [Testing](#testing)
- [Style Guidelines & Naming Conventions](#style_guidelines_and_naming_conventions)
- [Creating a Pull Request](#creating_a_pull_request)

<a name="roadmap"></a>
We use [Milestones](https://github.com/sendgrid/python-http-client/milestones) to help define current roadmaps, please feel free to grab an issue from the current milestone. Please indicate that you have begun work on it to avoid collisions. Once a PR is made, community review, comments, suggestions and additional PRs are welcomed and encouraged.

<a name="cla"></a>
## CLAs and CCLAs

Before you get started, SendGrid requires that a SendGrid Contributor License Agreement (CLA) or a SendGrid Company Contributor Licensing Agreement (CCLA) be filled out by every contributor to a SendGrid open source project.

Our goal with the CLA and CCLA is to clarify the rights of our contributors and reduce other risks arising from inappropriate contributions.  The CLA also clarifies the rights SendGrid holds in each contribution and helps to avoid misunderstandings over what rights each contributor is required to grant to SendGrid when making a contribution.  In this way the CLA and CCLA encourage broad participation by our open source community and help us build strong open source projects, free from any individual contributor withholding or revoking rights to any contribution.

SendGrid does not merge a pull request made against a SendGrid open source project until that pull request is associated with a signed CLA (or CCLA). Copies of the CLA and CCLA are available [here](https://drive.google.com/a/sendgrid.com/file/d/0B0PlcM9qA91LN2VEUTJWU2RIVXc/view).

You may submit your completed [CLA or CCLA](https://drive.google.com/a/sendgrid.com/file/d/0B0PlcM9qA91LN2VEUTJWU2RIVXc/view) to SendGrid at [dx@sendgrid.com](mailto:dx@sendgrid.com).  SendGrid will then confirm you are ready to begin making contributions.

There are a few ways to contribute, which we'll enumerate below:

<a name="feature_request"></a>
## Feature Request

If you'd like to make a feature request, please read this section.

The GitHub issue tracker is the preferred channel for library feature requests, but please respect the following restrictions:

- Please **search for existing issues** in order to ensure we don't have duplicate bugs/feature requests.
- Please be respectful and considerate of others when commenting on issues

<a name="submit_a_bug_report"></a>
## Submit a Bug Report

Note: DO NOT include your credentials in ANY code examples, descriptions, or media you make public.

A software bug is a demonstrable issue in the code base. In order for us to diagnose the issue and respond as quickly as possible, please add as much detail as possible into your bug report.

Before you decide to create a new issue, please try the following:

1. Check the Github issues tab if the identified issue has already been reported, if so, please add a +1 to the existing post.
2. Update to the latest version of this code and check if issue has already been fixed
3. Copy and fill in the Bug Report Template we have provided below

### Please use our Bug Report Template

In order to make the process easier, we've included a [sample bug report template](https://github.com/sendgrid/python-http-client/.github/ISSUE_TEMPLATE) (borrowed from [Ghost](https://github.com/TryGhost/Ghost/)). The template uses [GitHub flavored markdown](https://help.github.com/articles/github-flavored-markdown/) for formatting.

<a name="improvements_to_the_codebase"></a>
## Improvements to the Codebase

We welcome direct contributions to the python-http-client code base. Thank you!

### Development Environment ###

#### Install and Run Locally ####

##### Prerequisites #####

- Python 2.6 through 3.6
- There are no external dependencies

##### Initial setup: #####

```bash
git clone https://github.com/sendgrid/python-http-client.git
cd python-http-client
```

##### Execute: #####

See the [examples folder](https://github.com/sendgrid/python-http-client/tree/master/examples) to get started quickly.

<a name="understanding_the_codebase"></a>
## Understanding the Code Base

**/examples**

Working examples that demonstrate usage.

**/tests**

Unit and profiling tests.

**/python_http_client/client.py**

An HTTP client with a fluent interface using method chaining and reflection. By returning self on [__getattr__](https://github.com/sendgrid/python-http-client/blob/master/client.py#L74) and [_()](https://github.com/sendgrid/python-http-client/blob/master/client.py#L70), we can dynamically build the URL using method chaining and [__getattr__](https://github.com/sendgrid/python-http-client/blob/master/client.py#L74) allows us to dynamically receive the method calls to achieve reflection.

This allows for the following mapping from a URL to a method chain:

`/api_client/{api_key_id}/version` maps to `client.api_client._(api_key_id).version.<method>()` where <method> is a [HTTP verb](https://github.com/sendgrid/python-http-client/blob/master/client.py#L24).

**/python_http_client/config.py**

Loads the environment variables, if applicable.

<a name="testing"></a>
## Testing

All PRs require passing tests before the PR will be reviewed.

All test files are in the [`tests`](https://github.com/sendgrid/python-http-client/tree/master/tests) directory.

For the purposes of contributing to this repo, please update the [`test_unit.py`](https://github.com/sendgrid/python-http-client/blob/master/test/test_unit.py) file with unit tests as you modify the code.

For Python 2.6.*:

```bash
unit2 discover -v
```

For Python 2.7.* and up:

```bash
python -m unittest discover -v
```

<a name="testing_multiple_versoins_of_python"></a>
## Testing Multiple Versions of Python

All PRs require passing tests before the PR will be reviewed.

### Prequisites: ###

The above local "Initial setup" is complete

- [pyenv](https://github.com/yyuu/pyenv)
- [tox](https://pypi.python.org/pypi/tox)

### Initial setup: ###

Add `eval "$(pyenv init -)"` to your shell environment (.profile, .bashrc, etc) after installing tox, you only need to do this once.

```bash
pyenv install 2.6.9
pyenv install 2.7.11
pyenv install 3.4.3
pyenv install 3.5.2
pyenv install 3.6.0
python setup.py install
pyenv local 3.6.0 3.5.2 3.4.3 2.7.8 2.6.9
pyenv rehash
```

### Execute: ###

```bash
source venv/bin/activate
tox
```

<a name="style_guidelines_and_naming_conventions"></a>
## Style Guidelines & Naming Conventions

Generally, we follow the style guidelines as suggested by the official language. However, we ask that you conform to the styles that already exist in the library. If you wish to deviate, please explain your reasoning.

- [PEP8](https://www.python.org/dev/peps/pep-0008/)

Please run your code through:

- [pyflakes](https://pypi.python.org/pypi/pyflakes)
- [pylint](https://www.pylint.org/)
- [pep8](https://pypi.python.org/pypi/pep8)

## Creating a Pull Request<a name="creating_a_pull_request"></a>

1. [Fork](https://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/sendgrid/python-http-client
   # Navigate to the newly cloned directory
   cd sendgrid-python
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/sendgrid/python-http-client
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout <dev-branch>
   git pull upstream <dev-branch>
   ```

3. Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4a. Create tests.

4b. Create or update the example code that demonstrates the functionality of this change to the code.

5. Locally merge (or rebase) the upstream development branch into your topic branch:

   ```bash
   git pull [--rebase] upstream master
   ```

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

7. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description against the `master` branch. All tests must be passing before we will review the PR.

If you have any additional questions, please feel free to [email](mailto:dx@sendgrid.com) us or create an issue in this repo.
