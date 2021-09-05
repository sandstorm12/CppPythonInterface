# Class sample

A simple cpp class wrapped as a python class.

## Setup

Install Pybind11 library:
```bash
sudo apt install pybind11-dev python
sudo apt install python3.x-dev
```

** x would be your arbitray python version

## Use

Build the cpp file as a shared library:
```bash
cmake -DPYBIND11_PYTHON_VERSION=3.x . && cmake --build . --config Release
```

** x would be your arbitray python version

Run python code:
```bash
python3 main.py
```


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. Maybe add a benchmark.
