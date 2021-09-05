# Singleton Callback Joystick sample

A C++ class to find and read joystick events (Linux only). It only works for joysticks but with minor modification could work for any input device.

Some other examples are also included:
1. Reading joystick events using Pygame in Python
2. Reading joystick using linux file descriptors in Python

## Setup

Install Pybind11 library:
```bash
sudo apt install pybind11-dev python
sudo apt install python3.x-dev
python3 -m pip install pygame==2.0.1
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
or
```bash
python3 joystick_pygame.py
python3 joystick_file_descriptor.py
```



## Urgent issues
1. The singleton implementation is not right, the object is unique but the class is instantiated on import.


## Issues and future work
1. Maybe add a benchmark.
