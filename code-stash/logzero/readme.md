# *logzero* for Python logging

## Install logzero
```sh
$ pip3 install logzero
```
<br>

## Python logging levels
- The numeric values of logging levels are given in the following table. 
- These are primarily of interest if you want to define your own levels, and need them to have specific values relative to the predefined levels. 
- If you define a level with the same numeric value, it overwrites the predefined value; the predefined name is lost.

| Level | Numeric Value |
| --- | --- |
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |
<br>

## Default logging using logzero
Minimum log level in logzero is DEBUG
```python
import logging
import logzero

from logzero import logger


def display_logs() -> None:
    logger.debug("debug")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    logger.critical("critical")


print(f"Default logging level: {logging.getLevelName(logger.getEffectiveLevel())}")
display_logs()
```

![Alt text](ss/logzero1.png?raw=true "Default log level")
<br>

## Setting log level in logzero
```python
# change the log level
logzero.loglevel(level=0)
print(
    f"\nLogging level after changing log level to 0(NOTSET): {logging.getLevelName(logger.getEffectiveLevel())}"
)
display_logs()
```
![Alt text](ss/logzero2.png?raw=true "Custom set log level")
<br>

## Set custom formatter
```python
# Set custom formatter
formatter = LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s",
)
print("\nCustom Formatter")
logzero.formatter(formatter)
display_logs()
```
![Alt text](ss/logzero3.png?raw=true "Custom formatter")