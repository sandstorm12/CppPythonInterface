# Function interface with no arguments or return values

A simple cpp function that prints a string.

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

| Benchmark type     | Number of calls | Time python (secs) | Time c++ (secs) |
|--------------------|-----------------|--------------------|-----------------|
| Loop over function | 1000            | .000695            | .001619         |
| Loop over function | 10000           | .002697            | .015029         |
| Loop over function | 100000          | .025716            | .079801         |
| Loop over function | 1000000         | .265761            | .674001         |
| Loop in function   | 1000            | .000448            | .001177         |
| Loop in function   | 10000           | .002046            | .005005         |
| Loop in function   | 100000          | .019549            | .049472         |
| Loop in function   | 1000000         | .188696            | .493069         |


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
