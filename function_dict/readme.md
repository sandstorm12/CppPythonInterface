# Function interface dictionary

A number of simple cpp function to do simple operations on python dicts.

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

| Operation | Dictionary size | Time python (secs) | Time c++ (secs) |
|-----------|-----------------|--------------------|-----------------|
| Max       | 1000            | .00018             | .00006          |
| Max       | 1000000         | .07333             | .01927          |
| Sum       | 1000            | .00012             | .00004          |
| Sum       | 1000000         | .04445             | .01424          |
| Increment | 1000            | .00019             | .00011          |
| Increment | 1000000         | .07883             | .05548          |

## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
