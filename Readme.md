# Introduction 
This repository can be used as a template for small scale Visual Studio Python Projects. It includes a very simple python script (`template.py`) as well as a test script (`test_template.py`) that tests the functionalities defined in the *src/* directory. In addition the settings and launch file for this very simple setup can be found in the *.vscode* directory. The `settings.json` includes functionalites such as automatic linting (**flake8** and **pylint**), as well as automatic formatting with the **black** package (plus some more editor settings, like vertical ruler, etc.). The `launch.json`can be used to run the current python file as well as running a specific file with specified input arguments. 

# Getting Started

## Installation

In order to run this template project, some python packages as well as VS Code extensions are recommended if not required. The following packages will be listed in the following.

### Python and Virtual Environments

In order to work a python version **Python >= 3.6** is recommended, although also other **Python3.x** versions should work. In addition, a virtual environment is highly recommended for any Python Project. If running python inside a bash shell, personally I can only recommend the pip package **virtualenvwrapper** (although it is quite finicky to install in cygwin it works flawlessly in WSL). It allows to easily create and acess virtual environments that are saved in a single location on the system. A quick guide to this package can be found [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#). Otherwise, **virtualenv** or **venv** should do the trick.
Be sure to change the python path inside the `settings.json` file
```
"python.defaultInterpreterPath": "<path to virtual environment>"
```
You can also change the path inside the Command Palette (Ctrl+Shift+P -> Python:Select Interpreter) 

### Required Packages
You can run the script `template.py` out of the box. However, for all the linting, automatic formatting, etc. the following packages are required:
- linting/formatting (recommended: install the packages with conda or pip):
    - flake8
    - pylint
    - autopep8
    - black
- testing:
	- pytest
    - pytest-cov

You can find the requirements in the `requirements.txt` file and install them all at once using the 
command `pip install -r requirements.txt`

### (Optional) Extensions
There are hundreds of sites recommending all different python extensions that you need. The only one that I will recommend here though is the [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring), which really facilitates adding documentation to existing code.


# Build and Test
Run the script directly from the command line or by using the VS Code Debugger Tool and by selecting the appropriate launch configuration. 


# Contribute
To contribute to this project please contact me (Tobias Foresti) either by Teams or by email. I'm happy to add new features to this template, though I'd prefer to keep it simple so that it can be used for any purpose.