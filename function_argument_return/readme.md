# Function interface with no argument or return value

A simple cpp function interfaced with python to print hello world.

## Setup

Install Boost library:
```bash
sudo apt install pybind11-dev python
sudo apt install python3.x-dev
```

* x would be your arbitray python version

## Use

Build the cpp file as a shared library:
```bash
cmake -DPYBIND11_PYTHON_VERSION=3.8 . && cmake --build . --config Release
```

Run python code:
```bash
python3 main.py
```

## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
