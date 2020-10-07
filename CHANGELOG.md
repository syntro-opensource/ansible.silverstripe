# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.6] - 2020-07-15
### Fixed
* htaccess in root folder does now point to the Symlink

## [0.2.5] - 2020-07-14
### Added
* the role now creates a htaccess file in the project root, allowing said root to be used as webroot

## [0.2.4]
### Fixed
* Composer install command now is non-interactive
### Changed
* Composer install now uses optimized autoloader

## [0.2.3] - 2019-10-12
### Fixed
* The relative Logfile path now correctly renders if no `public/` dir is found.

## [0.2.2]
### Added
* Adds `ss_accept_host` parameter that defaults to `'yes'`
* The `release` process now creates a temp directory for the git module as workaround for [this issue](https://github.com/ansible/ansible/issues/30064)
### Changed
* reverting back to 0.2.0 as with_first_found searches on ansible host machine

## [0.2.1]
### Changed
* Key for git checkout now by default falls back to `~/.ssh/id_rsa` and omits it alltogether if this default file does not exist.

## [0.2.0]
### Added
* Added `ss_deploy_key` to indicate a deploy key file to use for checking out a private project

## [0.1.0]
### Added
* Initial Silverstripe deployment working
* Added Changelog


[Unreleased]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/0.2.6...develop
[0.2.5]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.5...0.2.6
[0.2.5]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.4...0.2.5
[0.2.4]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.3...v0.2.4
[0.2.3]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.2...v0.2.3
[0.2.2]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.1...v0.2.2
[0.2.1]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.2.0...v0.2.1
[0.2.0]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/compare/v0.1.0...v0.2.0
[0.1.0]: https://git.syntro.ch/services/silverstripe/ansible.silverstripe/tags/v0.1.0
