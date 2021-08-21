# Function interface with string as input and output

A number of simple cpp function to reverse a string.

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

## Benchmark

With O2 optimization on c++ implementation

| Operation       | String length   | Time python (secs) | Time c++ (secs) |
|-----------------|-----------------|--------------------|-----------------|
| Reverse         | 1000            | .000005            | .000063         |
| Reverse         | 1000000         | .000537            | .001417         |
| Count digits    | 1000            | .000233            | .000006         |
| Count digits    | 1000000         | .092724            | .000702         |


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
