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
You can set the minimum logging level using `loglevel()`
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
Use `LogFormatter` to change the color support, log format and date format.<br>
The following piece of code sets the formatter to display the method name along with the module name and line number:
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
<br>

## Add a custom log level
```python
APPLOG = 60
logzero.logging.addLevelName(APPLOG, "APPLOG")

def applog(self, message, *args, **kwargs):
    self.log(APPLOG, message, *args, **kwargs)

logzero.logging.Logger.applog = applog
print("\nCustom log level")
display_logs()
logger.applog("my applog")
```
![Alt text](ss/logzero4.png?raw=true "Custom log level")

## Modify formatting and colors
```python
# Add formatting and color to the custom log level
# also, change the color of existing log level
from logzero.colors import Fore as ForegroundColors
from logzero import DEFAULT_COLORS

DEFAULT_COLORS[APPLOG] = ForegroundColors.MAGENTA
DEFAULT_COLORS[logging.ERROR] = ForegroundColors.LIGHTRED_EX

formatter = LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(funcName)s:%(lineno)d]%(end_color)s %(message)s",
    colors=DEFAULT_COLORS,
)
logzero.formatter(formatter)
print("\nCustom log level and formatting")
display_logs()
logger.applog("my applog")
```
![Alt text](ss/logzero5.png?raw=true "Custom color formatting")