#include <iostream>
#include <pybind11/pybind11.h>


int count(int start, int length) {
    for (int i = start; i < start + length; i++) {
        std::cout << start + i << std::endl;
    }

    return start + length;
}

PYBIND11_MODULE(module, m)
{
    m.def("count", &count);
}
