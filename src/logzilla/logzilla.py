# ---------------------------------------------------------------------------------
# Copyright (c) Muhab Tomoum. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.
# ---------------------------------------------------------------------------------
"""
Author     : Muhab Tomoum
Description:
    wrapper around the `logging` standard library that provides a simpler more useful default.
    Quickly log to file and console in color and date/time stamped. The philosophy is simple
    only initialize the logger once at the beginning of your application and then use it where
    you need it. This will ensure that all loggers are configured the same way and that you can
    not accidentally create a new logger that is not configured the same way as the rest of your
    loggers.
"""


from __future__ import annotations

import datetime as dt
import inspect
import logging
import time
from pathlib import Path
from typing import Callable


class LogZilla:
    __initialized = False
    __log_folder_name = ".log"
    __date_format = "%Y/%m/%d %H:%M:%S"
    __default_prepend_info = "%(asctime)s: %(filename)s:%(lineno)s: %(levelname)s: %(message)s"
    __simple_prepend_info = "%(asctime)s: %(levelname)s: %(message)s"

    def __init__(self):
        raise RuntimeError(f"Do not instantiate {__class__} it is a singleton. You must use its class/static methods")

    @classmethod
    def init_root_logger(
        cls,
        output_dir: Path,
        log_file_name_append: str = "",
        min_level: int = logging.DEBUG,
        console_level: int = logging.INFO,
        file_level: int = logging.INFO,
        console_color_on: bool = True,
        file_color_on: bool = False,
        no_console_file_info: bool = False,
    ) -> None:
        """
        Initialize the logger to output to console and logfile.
        This function should be called only once from the main script.

        Example:
            Refer to main function at the end of this file

        Parameters:
            output_dir : folder where the `.log` folder is created and all log files are created
            log_file_name_append: append this string to the log file name if not specified it will default to
                the name of the file that called this function
            min_level : this is the minimum log level across all modules its best to keep this at DEBUG.
                e.g if this is logging.ERROR nothing lower severity such as info will be logged
            console_level : terminal print out level
            file_level : logfile print out level
            console_color_on : colored output to shell using ascii escape sequences
            file_color_on : color ascii escape sequences added to log file
            no_console_file_info: do not include file name and line number on console output
        """
        if cls.__initialized:
            raise RuntimeError("LogZilla already initialized.")
        if not log_file_name_append:
            caller_file = Path(inspect.stack()[1].filename)
            log_file_name_append = caller_file.stem

        log_file_name = dt.datetime.now().strftime(f"%Y.%m.%d_%H.%M.%S_{log_file_name_append}.log")
        log_file_dir = output_dir / cls.__log_folder_name
        log_file_dir = log_file_dir.absolute()
        log_file_path = log_file_dir / log_file_name

        if not log_file_dir.exists():
            log_file_dir.mkdir(parents=True)

        file_handler = logging.FileHandler(filename=log_file_path, encoding="utf-8", mode="w")

        console_formatter = None
        file_formatter = None

        if no_console_file_info:
            console_log_format = cls.__simple_prepend_info
        else:
            console_log_format = cls.__default_prepend_info

        if console_color_on:
            console_formatter = CustomFormatter(fmt=console_log_format, datefmt=cls.__date_format)
        else:
            console_formatter = logging.Formatter(fmt=console_log_format, datefmt=cls.__date_format)

        if file_color_on:
            file_formatter = CustomFormatter(fmt=cls.__default_prepend_info, datefmt=cls.__date_format)
        else:
            file_formatter = logging.Formatter(fmt=cls.__default_prepend_info, datefmt=cls.__date_format)

        errstream_handler = logging.StreamHandler()
        file_handler.setFormatter(file_formatter)
        errstream_handler.setFormatter(console_formatter)

        # get root logger
        logger = logging.getLogger()
        logger.setLevel(min_level)  # set global minimum level
        file_handler.setLevel(file_level)
        errstream_handler.setLevel(console_level)
        logger.addHandler(file_handler)
        logger.addHandler(errstream_handler)

        cls.__initialized = True
        logging.info("LogZilla: Root logger initialized.")

    @classmethod
    def log_title(cls, title: str, fill_char: str = "*", width=80):
        """Log a consistent section title."""
        logger = logging.getLogger(__name__)
        logger.info(f"{fill_char*width}")
        logger.info(f" {title} ".center(width, fill_char))
        logger.info(f"{fill_char*width}")

    @classmethod
    def log_execution_time(cls, func: Callable, log_level: int = logging.INFO) -> Callable:
        """log the execution time of the function passed in at info level
        this is intended to be used as a decorator.
        """
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            before = time.time()
            rv = func(*args, **kwargs)
            elapsed = time.time() - before
            elapsed = str(dt.timedelta(seconds=elapsed))
            logger.log(log_level, f"Execution Time of <{func.__name__ }>: {elapsed} hh:mm::ss")
            return rv

        return wrapper


class CustomFormatter(logging.Formatter):
    white = "\x1b[37;20m"
    green = "\x1b[32;20m"
    blue = "\x1b[34;20m"
    cyan = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt: str, datefmt: str) -> None:
        super().__init__(fmt, datefmt)
        self.FORMATS = {
            logging.DEBUG: self.cyan + fmt + self.reset,
            logging.INFO: self.green + fmt + self.reset,
            logging.WARNING: self.yellow + fmt + self.reset,
            logging.ERROR: self.red + fmt + self.reset,
            logging.CRITICAL: self.bold_red + fmt + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


@LogZilla.log_execution_time
def main() -> None:
    current_file_path = Path(__file__).absolute()
    current_file_dir = current_file_path.parent

    LogZilla.init_root_logger(
        output_dir=current_file_dir,
        console_level=logging.DEBUG,
        file_level=logging.DEBUG,
    )
    LogZilla.log_title("LogZilla Demo")

    logger = logging.getLogger(__name__)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    try:
        main()
    except Exception:  # pylint: disable=broad-except
        logging.exception("Exception caught at the main handler")
