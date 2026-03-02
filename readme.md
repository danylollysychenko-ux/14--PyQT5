## First things first:

When using external dependencies suck as (libararies installed with PIP), it is best to use python virutal (venv) to create isolated environments and avoid conflicts between projects.

## What is pip?

- "Preferred installation program" - package manager for python.
- Downloads and adds to your program, third party libraries from PyPI - Python Package Index

## Why use venv?

- When using Pip - you don't want to create version conflicts in your system - so you install dependecies at the project level.
- Venv is essentially a project level copy of python

### Setting up a venv

- in the terminal type `python -m venv venv` - or `python -m venv my_venv_folder`
  - This creates a folder named venv containing isolated environment
- now we have the resources for a virtual environment, but we have not activated it yet (so any installs would still be global)
- Activate the environment with (in windows) `venv/Scripts/activate`
  - You should then see something like `(venv) C:\Path\To\Your\Projects>`
- When you are done working in your virtual environment, you can exit it with `deactivate`

#### Freezing Requirements

- You should gitignore your `venv` folder, but you want to keep track of what needs to be installed for your program
  (whatever you pip installed) - To do this, you use a requirements.txt file. You can create it (while the venv is going) with `pip freeze > requirements.txt`
  - This will create a `requirements.txt` file.

#### Installing from requirements.txt

- If you pull your project down from github or other source control, you will need to create a virtual environment
  (you should do this), then you can install all dependencies with `pip install -r requirements.txt`

## PYQT5 - What is it?

- PYQT5 is a popular Python Library for creating Graphical User Inerfaces (GUIs) - pronounced "Gooey"

### Install PyQT5

- `pip install pyQt5`
  - Make sure you are in your virutal environment

- `pip freeze > requirements.txt`
  - this will create or update your requirements.txt file
