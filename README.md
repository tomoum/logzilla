# 1. Overview

`logzilla` is a simple yet capable python logging wrapper that gives you better defaults like coloured output.

# 2. Table of Contents

- [1. Overview](#1-overview)
- [2. Table of Contents](#2-table-of-contents)
- [3. Development](#3-development)
  - [3.1. Project Organization](#31-project-organization)
  - [3.2. `pyproject.toml`](#32-pyprojecttoml)
  - [3.3. Tools](#33-tools)
    - [3.3.1. black](#331-black)
    - [3.3.2. coverage](#332-coverage)
    - [3.3.3. pytest](#333-pytest)
    - [3.3.4. pylint](#334-pylint)
    - [3.3.5. pyright](#335-pyright)
    - [3.3.6. flake8](#336-flake8)
    - [3.3.7. tox](#337-tox)

# 3. Development

## 3.1. Project Organization

- `.vscode/settings.json`: Contains VSCode settings specific to the project, such as the Python interpreter to use and the maximum line length for auto-formatting.
- `src`: Place new source code here.
- `tests`: Contains Python-based test cases to validate source code.
- `pyproject.toml`: Contains metadata about the project and configurations for additional tools used to format, lint, type-check, and analyze Python code.

## 3.2. `pyproject.toml`

The pyproject.toml file is a centralized configuration file for modern Python projects. It streamlines the development process by managing project metadata, dependencies, and development tool configurations in a single, structured file. This approach ensures consistency and maintainability, simplifying project setup and enabling developers to focus on writing quality code. Key components include project metadata, required and optional dependencies, development tool configurations (e.g., linters, formatters, and test runners), and build system specifications.

In this particular pyproject.toml file, the [build-system] section specifies that the poetry package should be used to build the project. The [project] section provides metadata about the project, such as the name, description, authors, and classifiers.

The file also contains various configuration sections for different tools, including bandit, black, coverage, flake8, pyright, pytest, tox, and pylint. These sections specify settings for each tool, such as the maximum line length for flake8 and the minimum code coverage percentage for coverage.

## 3.3. Tools

### 3.3.1. black

Black is a Python code formatter that automatically reformats Python code to conform to the PEP 8 style guide. It is used to maintain a consistent code style throughout the project.

The pyproject.toml file specifies the maximum line length and whether or not to use a "fast" mode for formatting. Black also allows for a pyproject.toml configuration file to be included in the project directory to customize its behavior.

### 3.3.2. coverage

Coverage is a tool for measuring code coverage during testing. It generates a report of which lines of code were executed during testing and which were not.

The pyproject.toml file specifies that branch coverage should be measured and that the tests should fail if the coverage falls below 100%. Coverage can be integrated with a variety of test frameworks, including pytest.

### 3.3.3. pytest

Pytest is a versatile testing framework for Python projects that simplifies test case creation and execution. It supports both pytest-style and unittest-style tests, offering flexibility in testing approaches. Key features include fixture support for clean test environments, parameterized tests to reduce code duplication, and extensibility through plugins for customization. Adopt pytest to streamline testing and tailor the framework to your project's specific needs.

The pyproject.toml file plays an essential role in configuring pytest for your project. It includes various test markers, such as integration, notebooks, gpu, spark, slow, and unit, which are used during testing. It also specifies options for generating test coverage reports, setting the Python path, and outputting test results in the xunit2 format. You can easily modify the pyproject.toml file to customize pytest for your project's specific needs.

### 3.3.4. pylint
Pylint is a versatile Python linter and static analysis tool that identifies errors and style issues in your code. It generates an in-depth report, presenting errors, warnings, and conventions found in the codebase. Pylint configurations are centralized in the pyproject.toml file, covering extension management, warning suppression, output formatting, and code style settings such as maximum function arguments and class attributes. The unique scoring system provided by Pylint helps developers assess and maintain code quality, ensuring a focus on readability and maintainability throughout the project's development.

### 3.3.5. pyright

Pyright is a static type checker for Python that uses type annotations to analyze your code and catch type-related errors. It is capable of analyzing Python code that uses type annotations as well as code that uses docstrings to specify types.

The pyproject.toml file contains configurations for Pyright, such as the directories to include or exclude from analysis, the virtual environment to use, and various settings for reporting missing imports and type stubs. By using Pyright, you can catch errors related to type mismatches before they even occur, which can save you time and improve the quality of your code.

### 3.3.6. flake8
Flake8 is a code linter for Python that checks your code for style and syntax issues. It checks your code for PEP 8 style guide violations, syntax errors, and more.

The pyproject.toml file contains configurations for Flake8, such as the maximum line length, which errors to ignore, and which style guide to follow. By using Flake8, you can ensure that your code follows the recommended style guide and catch syntax errors before they cause problems.

### 3.3.7. tox
In our repository, we use Tox to automate testing and building our Python package across various environments and versions. Configured through the pyproject.toml file, Tox is set up with four testing environments: py, integration, spark, and all. Each environment targets specific test categories or runs all tests together, ensuring compatibility and functionality in different scenarios.

The [tool.tox] section in the pyproject.toml file contains the Tox configuration details, including the legacy_tox_ini attribute. Our setup outlines the dependencies needed for each environment, as well as the test runner (e.g., pytest) and any associated commands. This ensures consistent test execution across all environments.

Tox helps us efficiently automate testing and building processes, maintaining the reliability and functionality of our Python package across a wide range of environments. By identifying potential compatibility issues early in the development process, we improve the quality and usability of our package. Our Tox configuration streamlines the development workflow, promoting code quality and consistency throughout the project.



