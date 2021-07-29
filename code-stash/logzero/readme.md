# *logzero* for Python logging

## Install logzero
```sh
$ pip3 install logzero
```
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
## Set custom formatter
Use `formatter()` to change the log format string, color code for logging levels, and date format.
<p>The following piece of code sets the formatter to display the method name along with the module name and line number:</p>

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
## Add a custom log level
Register the new log level using `logging.addLevelName()`
<p>Here's an example, adding a new log level named <b>APPLOG</b> which has a value of <b>60</b>.</p>

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
## Modify/Set color code of the logging levels
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