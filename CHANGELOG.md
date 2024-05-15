<a name="unreleased"></a>
## [Unreleased]


<a name="1.2.1"></a>
## [1.2.1] - 2024-05-15
### 🍰 Added
- configurable logfile ([#43](https://github.com/syntro-opensource/ansible.silverstripe/issues/43))

### 🧬 Dependencies
- Bump actions/checkout from 3.0.2 to 4.1.5 ([#49](https://github.com/syntro-opensource/ansible.silverstripe/issues/49))


<a name="1.2.0"></a>
## [1.2.0] - 2022-09-10
### 🍰 Added
- package.json to automate release
- correctly transfer a graphql static dir ([#36](https://github.com/syntro-opensource/ansible.silverstripe/issues/36))

### 🐞 Fixed
- dependabot adds `Bump:` as prefix for updates

### 🔧 Changed
- tests run on pull

### 🧬 Dependencies
- robertdebock/galaxy-action from 1.1.1 to 1.2.1 ([#34](https://github.com/syntro-opensource/ansible.silverstripe/issues/34))
- robertdebock/molecule-action from 2.6.16 to 2.6.17 ([#18](https://github.com/syntro-opensource/ansible.silverstripe/issues/18))


<a name="1.1.0"></a>
## [1.1.0] - 2021-05-18
### 🍰 Added
- allow a custom htaccess template

### 🧬 Dependencies
- robertdebock/molecule-action from 2.6.8 to 2.6.16 ([#15](https://github.com/syntro-opensource/ansible.silverstripe/issues/15))
- robertdebock/galaxy-action from 1.1.0 to 1.1.1 ([#16](https://github.com/syntro-opensource/ansible.silverstripe/issues/16))


<a name="1.0.4"></a>
## [1.0.4] - 2021-04-07
### 🐞 Fixed
- dependabot uses correct ecosystem for actions

### 🔧 Changed
- use items() for extra variables loop

### 🧬 Dependencies
- robertdebock/molecule-action from 2.6.3 to 2.6.4 ([#12](https://github.com/syntro-opensource/ansible.silverstripe/issues/12))


<a name="1.0.3"></a>
## [1.0.3] - 2020-11-02
### 🐞 Fixed
- mv does not fail anymore because of second `-f` flag


<a name="1.0.2"></a>
## [1.0.2] - 2020-10-23
### 🔧 Changed
- step to ensure presence of vars now enforces string to allow vaulted vars


<a name="1.0.1"></a>
## [1.0.1] - 2020-10-14
### 🍰 Added
- release badge
- test badge
- badges to readme

### 🐞 Fixed
- galaxy import ([#7](https://github.com/syntro-opensource/ansible.silverstripe/issues/7))

### 🔧 Changed
- update download command

### 🗑 Removed
- red
- no longer use automatic changelog workflow

### Pull Requests
- Merge pull request [#5](https://github.com/syntro-opensource/ansible.silverstripe/issues/5) from syntro-opensource/master


<a name="1.0.0"></a>
## 1.0.0 - 2020-10-07
### 🍰 Added
- Chglog config ([#2](https://github.com/syntro-opensource/ansible.silverstripe/issues/2))
- Galaxy publish
- changelog workflow
- Code of Conduct
- molecule testing ([#1](https://github.com/syntro-opensource/ansible.silverstripe/issues/1))
- license
- initial commit

### Pull Requests
- Merge pull request [#4](https://github.com/syntro-opensource/ansible.silverstripe/issues/4) from syntro-opensource/release/1.0.0


[Unreleased]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.2.1...HEAD
[1.2.1]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.0.4...1.1.0
[1.0.4]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.0.3...1.0.4
[1.0.3]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.0.2...1.0.3
[1.0.2]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/syntro-opensource/ansible.silverstripe/compare/1.0.0...1.0.1
