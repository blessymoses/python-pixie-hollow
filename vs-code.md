# VS Code

## Set up Python Black Formatter
In Settings(`File -> Preferences -> Settings` or <kbd>ctrl</kbd> + <kbd>,</kbd>),
* Search for `format on save` and check - Format a file on save. 
* Search for `python formatting provider` and select `black`.
* Edit and save a python file. Install black when prompted.

## Enable intellisense for Python in VS Code
* Open `command palette` - <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>
* Type `Python:Select Interpreter` and select.
* Re-open VS Code.

## Keep the tabs open by default
VS code opens a file in *Preview mode* by default. 
To disable preview mode, 
* Search for `workbench.editor.enablepreview` in Settings, and uncheck.
* Alternatively, set `workbench.editor.enablePreview: false` in settings.json file.

---
# Python Trivia

## Python CLI
1. The Python interpreter takes option **-c** for **command**, which says to execute the Python command line arguments following the option -c as a Python program.
    ```shell
    $ python -c "print('Hello')"
    Hello
    ```

## Online Terminals
1. https://replit.com/languages/python3
2. https://www.python.org/shell/
3. https://www.programiz.com/python-programming/online-compiler/