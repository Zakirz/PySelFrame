from collections import OrderedDict
import logging

from Core.Configs import RunConfig
import textwrap
import sys


class Logger(RunConfig):
    @property
    def logger(self):
        name = self.__class__.__name__
        extra = {"logid": self.LOG_ID}
        logger = logging.getLogger(name)
        logger = logging.LoggerAdapter(logger, extra)
        return logger

    def init_logger(self):
        __log_level = logging.INFO
        __formatter = "%(levelname)-8s | %(asctime)s | %(message)s"
        __handlers = [
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(filename=f"{self.LOG_FILE}", mode="w")
        ]

        # noinspection PyArgumentList
        logging.basicConfig(
            level=__log_level,
            format=__formatter,
            handlers=__handlers
        )
        self.logger.info("Initializing logger...")

    def log_writer(self, *, level: str, message: str):
        try:
            self.LOG_ID += 1
            if level is None:
                level = "INFO"

            if not level.isupper():
                level = level.upper()

            write_log = OrderedDict({
                "DEBUG": self.logger.info,
                "INFO": self.logger.info,
                "WARNING": self.logger.warning,
                "ERROR": self.logger.error,
                "CRITICAL": self.logger.critical,
                "EXCEPTION": self.logger.error
            })

            write_log[level](message)
        except KeyError:
            self.logger.warning(f"{level} is not a valid Log Level")
            self.logger.info(message)

    def log(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.log_writer(level='INFO', message=message)

    def error(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.log_writer(level='ERROR', message=message)

    def fatal(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.log_writer(level='CRITICAL', message=message)
