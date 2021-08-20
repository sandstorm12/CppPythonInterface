#include <iostream>
#include <pybind11/pybind11.h>


void print_hello_world() {
    std::cout << "Hello World" << std::endl;
}

PYBIND11_MODULE(module, m)
{
    m.def("print_hello_world", &print_hello_world);
}
