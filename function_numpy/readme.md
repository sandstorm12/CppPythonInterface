# Function NumPy

Simple sample to demonstrate the use of numpy arrays in c++ using pybind11.

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

| Operation       | Array shape     | Time python (secs) | Time python numpy (secs) | Time c++ (secs) |
|-----------------|-----------------|--------------------|--------------------------|-----------------|
| Print shape     | 1000x1000       | .000015            | -                        | .000118         |
| Print shape     | 10000x10000     | .000015            | -                        | .000118         |
| Increment       | 1000x1000       | .541431            | .000840                  | .001224         |
| Increment       | 10000x10000     | 81.0391            | .121430                  | .105277         |
| Sum             | 1000x1000       | .251272            | .000518                  | .001068         |
| Sum             | 10000x10000     | 37.4717            | .056698                  | .138734         |


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. Refactor.
