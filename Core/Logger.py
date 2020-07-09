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
        __formatter = "%(levelname)-8s | %(logid)-4s | %(asctime)s | %(message)s"
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

    def info_log(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.LOG_ID += 1
        self.logger.info(message)

    def warn_log(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.LOG_ID += 1
        self.logger.warning(message)

    def fail_log(self, message: str):
        wrapper = textwrap.TextWrapper(width=120)
        message = wrapper.fill(message.strip())
        self.LOG_ID += 1
        self.logger.error(message)
