import logging
import logzero

from logzero import logger, LogFormatter


def display_logs() -> None:
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    logger.critical("critical")


print(f"Default logging level: {logging.getLevelName(logger.getEffectiveLevel())}")
print("\nDefault Formatter")
display_logs()

# change the log level
logzero.loglevel(level=0)
print(
    f"\nLogging level after changing log level to 0(NOTSET): {logging.getLevelName(logger.getEffectiveLevel())}"
)
display_logs()

logzero.loglevel(level=logging.DEBUG)

# Set custom formatter for log line
formatter = LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s",
)
print("\nCustom Formatter for log line")
logzero.formatter(formatter)
display_logs()

# Add custom log level
APPLOG = 60
logzero.logging.addLevelName(APPLOG, "APPLOG")


def applog(self, message, *args, **kwargs):
    self.log(APPLOG, message, *args, **kwargs)


logzero.logging.Logger.applog = applog
print("\nAfter adding log level with value 60")
display_logs()
logger.applog("my applog")

# Add color to the custom log level and change the color of existing log level
from logzero.colors import Fore as ForegroundColors
from logzero import DEFAULT_COLORS

DEFAULT_COLORS[APPLOG] = ForegroundColors.MAGENTA
DEFAULT_COLORS[logging.ERROR] = ForegroundColors.LIGHTRED_EX

color_formatter = LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s",
    colors=DEFAULT_COLORS,
)
logzero.formatter(color_formatter)
print("\nCustom color for log levels")
display_logs()
logger.applog("my applog")
