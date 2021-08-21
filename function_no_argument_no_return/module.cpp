#include <iostream>
#include <pybind11/pybind11.h>


void print_hello_world() {
    std::cout << "Hello World" << std::endl;
}


void print_hello_world_repeat(int count) {
    for (int i = 0; i < count; i++) {
        std::cout << "Hello World" << std::endl;
    }
}


PYBIND11_MODULE(module, m)
{
    m.def("print_hello_world", &print_hello_world);
    m.def("print_hello_world_repeat", &print_hello_world_repeat);
}
