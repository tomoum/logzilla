# 1. Overview

*logzilla* is a simple yet capable python logging wrapper that gives you better defaults like coloured output.

# 2. Table of Contents

- [1. Overview](#1-overview)
- [2. Table of Contents](#2-table-of-contents)
- [3. Installation and usage](#3-installation-and-usage)
  - [3.1. Installation](#31-installation)
  - [3.2. Examples](#32-examples)
  - [3.3. Example 1: Minimal example](#33-example-1-minimal-example)
  - [3.4. Example 2: No file info to console](#34-example-2-no-file-info-to-console)
- [4. Other Docs](#4-other-docs)
- [5. Future Improvements](#5-future-improvements)

# 3. Installation and usage

## 3.1. Installation

It requires Python 3.8.1+ to run.
`pip install logzilla`

## 3.2. Examples

In both examples a `.log` folder is created in the output directory with the
following files corresponding to the date and time of execution of each example:

- `2023.04.10 15.54.23_logzilla.log`
- `2023.04.10 16.18.29_logzilla.log`

Sample log file output:

```log
2023/04/10 15:55:16: logzilla.py:115: INFO: LogZilla: Root logger initialized.
2023/04/10 15:55:16: logzilla.py:121: INFO: ********************************************************************************
2023/04/10 15:55:16: logzilla.py:122: INFO: ******************************** LogZilla Demo *********************************
2023/04/10 15:55:16: logzilla.py:123: INFO: ********************************************************************************
2023/04/10 15:55:16: logzilla.py:183: DEBUG: debug message
2023/04/10 15:55:16: logzilla.py:184: INFO: info message
2023/04/10 15:55:16: logzilla.py:185: WARNING: warning message
2023/04/10 15:55:16: logzilla.py:186: ERROR: error message
2023/04/10 15:55:16: logzilla.py:187: CRITICAL: critical message
2023/04/10 15:55:16: logzilla.py:137: INFO: Execution Time of <main>: 0:00:00.012001 hh:mm::ss
```

## 3.3. Example 1: Minimal example

```python
@log_execution_time
def main() -> None:
    current_file_path = Path(__file__).absolute()
    current_file_dir = current_file_path.parent

    LogZilla.init_root_logger(
        output_dir=current_file_dir,
        console_level=logging.DEBUG,
        file_level=logging.DEBUG,
    )
    log_title("LogZilla Demo")

    logger = logging.getLogger(__name__)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
```

Output:

![simple_example](https://github.com/tomoum/logzilla/blob/main/docs/assets/simple_example.png?raw=true)

## 3.4. Example 2: No file info to console

```python
@log_execution_time
def main() -> None:
    current_file_path = Path(__file__).absolute()
    current_file_dir = current_file_path.parent

    LogZilla.init_root_logger(
        output_dir=current_file_dir,
        console_level=logging.DEBUG,
        file_level=logging.DEBUG,
        no_console_file_info=True,
    )
    log_title("LogZilla Demo")

    logger = logging.getLogger(__name__)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
```

Output:
![no_file_info_to_console](https://github.com/tomoum/logzilla/blob/main/docs/assets/no_file_info_to_console.png?raw=true)

# 4. Other Docs

- [Developer](docs/developer.md)

# 5. Future Improvements

- add unit tests
- add pre-commit hooks for `black, pylint, flake8, bandit, tox, pytest` for development environment
