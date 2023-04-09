# 1. Poetry

Main tool that manages the project dev environment, building and publishing.

# 2. Table of Contents

- [1. Poetry](#1-poetry)
- [2. Table of Contents](#2-table-of-contents)
- [3. One Time Setup per Host/Environment](#3-one-time-setup-per-hostenvironment)
  - [3.1. Pypi test](#31-pypi-test)
  - [3.2. Pypi Production](#32-pypi-production)
  - [3.3. Each time you need to publish](#33-each-time-you-need-to-publish)
    - [3.3.1. Bump version](#331-bump-version)
    - [3.3.2. Poetry Publish](#332-poetry-publish)

# 3. One Time Setup per Host/Environment

## 3.1. Pypi test

- add repository to poetry config
    `poetry config repositories.test-pypi https://test.pypi.org/legacy/`

- get token from [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/)

- store token using `poetry config pypi-token.test-pypi pypi-YYYYYYYY`

> Note: 'test-pypi' is the name of the repository

## 3.2. Pypi Production

- get token from [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
- store token using `poetry config pypi-token.pypi pypi-XXXXXXXX`

## 3.3. Each time you need to publish

### 3.3.1. Bump version

- `poetry version prerelease` or
- `poetry version patch`

### 3.3.2. Poetry Publish

To [TestPyPi](https://test.pypi.org/)

- `poetry publish -r test-pypi`

To [PyPi](https://pypi.org/)

- `poetry publish`
