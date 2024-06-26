# PickleTestSuite

## Introduction

Our goal is to assess the stability and correctness of the Python pickle module by investigating whether identical inputs consistently produce hash-identical serialized outputs. We define identical inputs as those generating the same pickle file under all circumstances, including different operating systems, Python versions (excluding changes to pickle), floating-point precision, and recursive data structures. Our task is to develop a comprehensive test suite to rigorously evaluate pickle's stability and correctness, ensuring reproducibility of all results and findings.

Some information about pickle:
> The [pickle](). module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a [binary file](https://docs.python.org/3/glossary.html#term-binary-file) or bytes-like object(https://docs.python.org/3/glossary.html#term-bytes-like-object)) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1](https://docs.python.org/3/library/pickle.html#id7) or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
> [Source](https://docs.python.org/3/library/pickle.html)

## How to Use - Local
### Prerequisites
You need to have python installed and some familarity with it and pip. All the project specfic files can be found in the [requirements](requirements.txt) file.

These can be downloaded using the following shell command.
``` BASH
pip install -r requirements.txt

```

Note: Pickle is a part of the standard library, atleast for python3.

### Run

To run any file you can
``` BASH
python3 FILENAME.py

```

All of the test can also be run using pytest.
``` BASH
pytest

```

An alternativ if you want to test multiple versions of python is 
``` BASH
tox

```
However, to do that you need to have the interpreters already installed. This can be done through the shell script found [here](./install_pyenv_ubuntu.sh). However, that is only for ubuntu right now. MacOS works, but windows does not right now for pyenv. If running tox you find test skipped, that is beacuse they are not installed. That can be done using the provided [Makefile](./Makefile). If the pyenv doesn't work with the script, run `source ~/.bashrc` or `exec "$SHELL"` to update the paths and restart the terminal.

## How to Use - DevContainer
### Prerequisites

You need to have docker installed on your computer. It's also helpful to have the vscode [devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) exstension.

To open the container, simply press ´ctrl + shift + p´ and select
>Dev Containers: Reopen in container

After waiting for a while, you'll have the entire enviroment needed to run the project.

### Run

To run any file you can
``` BASH
python3 FILENAME.py

```

All of the test can also be run using pytest.
``` BASH
pytest

```

An alternativ if you want to test multiple versions of python is 
``` BASH
tox

```
However, to do that you need to have the interpreters already installed. This can be done through the shell script found [here](./install_pyenv_ubuntu.sh). However, that is only for ubuntu right now. MacOS works, but windows does not right now for pyenv. If running tox you find test skipped, that is beacuse they are not installed. That can be done using the provided [Makefile](./Makefile). If the pyenv doesn't work with the script, run `source ~/.bashrc` or `exec "$SHELL"` to update the paths and restart the terminal.

## Running workflows

This project has many workflows and to some extent is based upon them. There is one base workflow that will run on any commit that is coming into main. THe other one is a bit more interesting however. This is the workflow that runs our tests over multiple versions and OS automatically. However for it to run, we need to start it ourselves. This can be done on github by clicking on the *[Actions](https://github.com/Uplink036/PickleTestSuite/actions)* tab, 

## License

Author(s) - Oliver Sjödin, Adam Mützell, Tobias Mattsson

Licensed under the [MIT License](LICENSE)