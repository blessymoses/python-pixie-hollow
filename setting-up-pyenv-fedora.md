# Setting up pyenv in Fedora

pyenv is a tool for managing multiple Python versions.

### Why pyenv?
* easily switch between multiple versions of Python. 
* try out new language features in different versions of Python.


## Installation

1. **Install build dependencies**

        dnf install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev python-openssl git openssl-devel

        dnf install -y --skip-broken git gcc zlib-devel bzip2-devel readline-devel sqlite-devel
    
    You can find the platform-specific build dependencies in https://github.com/pyenv/pyenv/wiki#suggested-build-environment and https://github.com/pyenv/pyenv/wiki/Common-build-problems#prerequisites


2. **Check out pyenv**
    
    Check out pyenv where you want it installed.

        git clone https://github.com/pyenv/pyenv.git ~/.pyenv


3. **Define environment variables**
    
    Define environment variables `PYENV_ROOT` to point to the path where pyenv repo is cloned and add `$PYENV_ROOT/bin` to your `$PATH` for access to the `pyenv` command-line utility.

    ~~~ bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    ~~~


4. **Enable shims and autocompletion**
    
    Add `pyenv init` to your shell and make sure `eval "$(pyenv init -)"` is placed toward the end of the shell configuration file since it manipulates `PATH` during the initialization.

    ~~~ bash
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    ~~~


5. **Restart Shell**
   
    Restart your shell so the path changes take effect.
    ```sh
    exec "$SHELL"
    ```

    You can now begin to use pyenv.
    ```sh
    $ pyenv
    pyenv 1.2.26-11-g6759b7cd
    Usage: pyenv <command> [<args>]

    $ pyenv versions
    * system (set by /home/blessy/.pyenv/version)
    ```
    
6. **Install a version of Python in pyenv**
    ```sh
    $ pyenv install 3.9.0
    ``` 
    If you list the python versions in pyenv, you can find all the versions that are installed.
    ```sh
    $ pyenv versions
    * system (set by /home/blessy/.pyenv/version)
      3.9.0
    ```
    To activate a Python version,
    ```sh
    $ pyenv shell 3.9.0
    $ python --version
    Python 3.9.0
    ```
### Additional reading
- https://realpython.com/intro-to-pyenv/

# Using venv

* venv is a default package shipped with Python 3, which supports creating lightweight virtual environments.

1. To create a new virtual environment:
    ```sh
    $ python3 -m venv myenv
    ```
2. To activate the virtual environment:
    ```sh
    $ source myenv/bin/activate
    (myenv) $
    ```
3. To deactivate the virtual environment:
    ```sh
    $ deactivate
    ```