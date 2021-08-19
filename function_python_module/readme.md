# Function interface dict argument

Function interface using python dict.

## Setup

Install Boost library:
```bash
sudo apt-get install libboost-all-dev
sudo apt-get install python-dev libxml2-dev libxslt-dev
```

## Use

Build the cpp file as a shared library:
```bash
cmake . && cmake --build . --config Release
```

Run python code:
```bash
python3 main.py
```

## Benchmark
| Iterations | Python time (sec) | C++ time (sec) |
|------------|-------------------|----------------|
| 1000       | .0007             | .0010          |
| 10000      | .0040             | .0036          |

## Urgent issues
1. [Nothing yet]


## Issues and future work
1. Why item assignment for python objects in C++ is so slow?
