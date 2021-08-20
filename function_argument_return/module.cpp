#include <iostream>
#include <pybind11/pybind11.h>


int count(int length) {
    int counter = 1;
    for (int i = 0; i < length; i++) {
        counter += counter;
    }

    return counter;
}

PYBIND11_MODULE(module, m)
{
    m.def("count", &count);
}
