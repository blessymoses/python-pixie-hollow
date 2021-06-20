import logging
import logzero

from logzero import logger, LogFormatter


def display_logs() -> None:
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    logger.critical("critical")


# print(f"Default logging level: {logging.getLevelName(logger.getEffectiveLevel())}")
print("\nDefault Formatter")
display_logs()

# # change the log level
# logzero.loglevel(level=0)
# print(
#     f"\nLogging level after changing log level to 0(NOTSET): {logging.getLevelName(logger.getEffectiveLevel())}"
# )
# display_logs()

# Set custom formatter
formatter = LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s",
)
print("\nCustom Formatter")
logzero.formatter(formatter)
display_logs()