#include <iostream>
#include <boost/python.hpp>


void print_hello_world() {
    std::cout << "Hello World" << std::endl;
}

BOOST_PYTHON_MODULE(module)
{
    boost::python::def("print_hello_world", print_hello_world);
}
