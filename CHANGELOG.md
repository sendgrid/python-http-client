# Change Log
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).

## [2.2.1] - 2016-08-10
### Fixed
- When Content-Type is not application/json, do not JSON encode the request body

## [2.2.0] - 2016-08-10
### Added
- Ability to set the Content-Type header

## [2.1.1] - 2016-07-08
### Fixed
- [Allow multiple values for a parameter](https://github.com/sendgrid/python-http-client/pull/11)
- Thanks [Chris Henry](https://github.com/chrishenry)!

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
- Thanks to [Kevin Gillette](https://github.com/extemporalgenome)!
- Update of request headers simplified
- Thanks to [Matt Bernier](https://github.com/mbernier)

## [1.1.3] - 2016-02-29
### Fixed
- Various standardizations for commenting, syntax, pylint
- Thanks to [Ian Douglas](https://github.com/iandouglas)!

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