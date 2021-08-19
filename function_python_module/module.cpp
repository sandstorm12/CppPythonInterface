#include <iostream>
#include <boost/python.hpp>

int main() {
    Py_Initialize();
    
    boost::python::object numpy = boost::python::import("numpy");
    
    boost::python::object array = numpy.attr("zeros")(
        boost::python::make_tuple(10, 10)
    );
    boost::python::tuple shape = (boost::python::tuple) array.attr("shape");
    std::cout
        << boost::python::extract<std::string>(boost::python::str(shape))()
        << std::endl;

    return 0;
}