# Function interface with argument and return value

A number of simple cpp function to count to a number and return the counted value.

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

| Count length    | Time python (secs) | Time c++ (secs) |
|-----------------|--------------------|-----------------|
| 1000            | .000192            | .000077         |
| 10000           | .004942            | .000079         |
| 100000          | .129831            | .000183         |
| 1000000         | 16.4190            | .001124         |


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
