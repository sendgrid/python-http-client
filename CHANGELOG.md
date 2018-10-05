# Change Log
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).

## [3.1.0] - 2018-05-23
### Added
- [Update register.py to use pypandoc](https://github.com/sendgrid/python-http-client/commit/6a3a63e2511b3df9c9ef23eebd5bcd80ad8821ae)
- [PR #21](https://github.com/sendgrid/python-http-client/pull/21): Support timeout. Thanks, [George Kussumoto](https://github.com/georgeyk)!
- [PR #22](https://github.com/sendgrid/python-http-client/pull/22): Client can be pickled and unpickled. Thanks, [Jussi Heikkilä](https://github.com/jussih)!
- [PR #26](https://github.com/sendgrid/python-http-client/pull/26): Create CODE_OF_CONDUCT.md. Thanks, [Fredrik Svensson](https://github.com/SvenssonWeb)!
- [PR #30](https://github.com/sendgrid/python-http-client/pull/30): Create TROUBLESHOOTING.md. Thanks, [Omer Ahmed Khan](https://github.com/OmerAhmedKhan)!
- [PR #33](https://github.com/sendgrid/python-http-client/pull/33): Update README.md badges and license. Thanks, [Alfred Gutierrez](https://github.com/alfg)!
- [PR #34](https://github.com/sendgrid/python-http-client/pull/34): Update .md files for SEO. Thanks, [Gustavo Siqueira](https://github.com/gugsrs)!
- [PR #36](https://github.com/sendgrid/python-http-client/pull/36): Added more badges to README.md. Thanks,, [Shivam Agarwal](https://github.com/gr8shivam)!
- [PR #41](https://github.com/sendgrid/python-http-client/pull/41): Added License link to README ToC. Thanks,, [Andrew Joshua Loria](https://github.com/ajloria)!
- [PR #49](https://github.com/sendgrid/python-http-client/pull/49): Add USAGE.md. Thanks, [Adelmo Junior](https://github.com/noblehelm)!
- [PR #43](https://github.com/sendgrid/python-http-client/pull/43): Add PULL_REQUEST_TEMPLATE. Thanks, [Aleksandr Sobolev](https://github.com/s0b0lev)!
- [PR #50](https://github.com/sendgrid/python-http-client/pull/50): Add Docker files and update README. Thanks, [Stanley Ndagi](https://github.com/NdagiStanley)!
- [PR #69](https://github.com/sendgrid/python-http-client/pull/69): Simplify GitHub PR template. Thanks, [Alex](https://github.com/pushkyn)!
- [PR #61](https://github.com/sendgrid/python-http-client/pull/61): License date range UnitTest. Thanks, [Anfernee Sodusta](https://github.com/dinosaurfiles)!
- [PR #60](https://github.com/sendgrid/python-http-client/pull/60): Adds test for repo files. Thanks, [Cheuk Yin Ng](https://github.com/cheukyin699)!
- [PR #47](https://github.com/sendgrid/python-http-client/pull/47): Add .env_sample file. Thanks, [Rod Xavier](https://github.com/rodxavier)!
- [PR #66](https://github.com/sendgrid/python-http-client/pull/66): Update travis.yml to fail on Pep8 errors. Thanks, [Stanley Ndagi](https://github.com/NdagiStanley)!
- [PR #67](https://github.com/sendgrid/python-http-client/pull/67): Made python-http-client comply with autopep8. Thanks, [Madhur Garg](https://github.com/Madhur96)!
- [PR #81](https://github.com/sendgrid/python-http-client/pull/81): PEP8 updates. Thanks, [~](https://github.com/delirious-lettuce)!
- [PR #73](https://github.com/sendgrid/python-http-client/pull/73): Add CodeCov support to .travis.yml. Thanks, [Senthil](https://github.com/senthilkumar-e)!
- [PR #77](https://github.com/sendgrid/python-http-client/pull/77): Include code review in README.md. Thanks, [Jared Scott](https://github.com/jlax47)!
- [PR #87](https://github.com/sendgrid/python-http-client/pull/87): Add manifest that includes the license in sdist. Thanks, [RohitK89](https://github.com/RohitK89)!

### Fixed
- [PR #24](https://github.com/sendgrid/python-http-client/pull/24): Fix Typo in CONTRIBUTING.md. Thanks, [Cícero Pablo](https://github.com/ciceropablo)!
- [PR #23](https://github.com/sendgrid/python-http-client/pull/23): Fix Typo in README.md. Thanks, [Cícero Pablo](https://github.com/ciceropablo)!
- [PR #28](https://github.com/sendgrid/python-http-client/pull/28): Fix Travis CI Build. Thanks, [Kevin Anderson](https://github.com/kevinanderson1)!
- [PR #40](https://github.com/sendgrid/python-http-client/pull/40): Update contributing and readme - fix typo, ToC. Thanks, [Alex](https://github.com/pushkyn)!
- [PR #54](https://github.com/sendgrid/python-http-client/pull/54): Fix code style issues. Thanks, [Stephen James](https://github.com/StephenOrJames)!
- [PR #82](https://github.com/sendgrid/python-http-client/pull/82): PEP8 updates. Thanks, [~](https://github.com/delirious-lettuce)!
- [PR #83](https://github.com/sendgrid/python-http-client/pull/83): Fix Travis build errors. Thanks, [~](https://github.com/delirious-lettuce)!
- [PR #84](https://github.com/sendgrid/python-http-client/pull/84): Fix docstring variable name. Thanks, [~](https://github.com/delirious-lettuce)!
- Fix [Issue #86](https://github.com/sendgrid/python-http-client/issues/86): Error converting Response.to_dict.

## [3.0.0] - 2017-08-11
### BREAKING CHANGE
- The breaking change actually happened in [version 2.3.0](https://github.com/sendgrid/python-http-client/releases/tag/v2.3.0), which I mistakenly applied a minor version bump.
- This version replaces error handling via HTTPError from urllib in favor of custom error handling via the [HTTPError class](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py).

## [2.4.0] - 2017-07-03
### Added
- #19 Added support for slash. Created "to_dict" property in response object and exception class.
- Thanks, [Lucas Cardoso](https://github.com/MrLucasCardoso)!

## [2.3.0] - 2017-06-20
### Added
- #17 Added support for error handling
- Thanks, [Dibya Prakash Das](https://github.com/dibyadas)!

## [2.2.1] - 2016-08-10
### Fixed
- When Content-Type is not application/json, do not JSON encode the request body

## [2.2.0] - 2016-08-10
### Added
- Ability to set the Content-Type header

## [2.1.1] - 2016-07-08
### Fixed
- [Allow multiple values for a parameter](https://github.com/sendgrid/python-http-client/pull/11)
- Thanks, [Chris Henry](https://github.com/chrishenry)!

## [2.1.0] - 2016-06-03
### Added
- Automatically add Content-Type: application/json when there is a request body

## [2.0.0] - 2016-06-03
### Changed
- Made the Response variables non-redundant. e.g. response.response_body becomes response.body

## [1.2.4] - 2016-03-02
### Fixed
- Getting README to display in PyPi

## [1.2.3] - 2016-03-01
### Added
- Can now reuse part of the chaining construction for multiple urls/requests
- Thanks, to [Kevin Gillette](https://github.com/extemporalgenome)!
- Update of request headers simplified
- Thanks, to [Matt Bernier](https://github.com/mbernier)

## [1.1.3] - 2016-02-29
### Fixed
- Various standardizations for commenting, syntax, pylint
- Thanks, to [Ian Douglas](https://github.com/iandouglas)!

## [1.1.2] - 2016-02-29
### Fixed
- Fixed TypeError in Python 3+ for data encoding

## [1.1.1] - 2016-02-25
### Updated
- Tests no longer require a mock server [#5](https://github.com/sendgrid/python-http-client/pull/5)

## [1.1.0] - 2016-02-25
### Fixed
- Config paths

## [1.0.2] - 2016-02-25
### Fixed
- Config paths

## [1.0.1] - 2016-02-25
### Fixed
- Imports

## [1.0.0] - 2016-02-25
### Added
- We are live!