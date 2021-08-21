# Function interface list

A number of simple cpp function to do simple operations on python lists.

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

| Operation | list size       | Time python (secs) | Time c++ (secs) |
|-----------|-----------------|--------------------|-----------------|
| Max       | 1000            | .000075            | .000053         |
| Max       | 1000000         | .025735            | .013022         |
| Sum       | 1000            | .000128            | .000024         |
| Sum       | 1000000         | .049666            | .006538         |
| Increment | 1000            | .000189            | .000087         |
| Increment | 1000000         | .078299            | .036218         |


## Urgent issues
1. [Nothing yet]


## Issues and future work
1. [Nothing yet]
