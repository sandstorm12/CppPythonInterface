#include <iostream>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>


void print_shape(pybind11::array_t<double> &numpy_array) {
    pybind11::buffer_info buffer = numpy_array.request();
    for (int i = 0; i < int(buffer.shape.size()); i++) {
        pybind11::print("Dimension", i, ": ", buffer.shape[i]);
    }
}


pybind11::array_t<double> increment(pybind11::array_t<double> &numpy_array) {
    pybind11::buffer_info buffer = numpy_array.request();
    double *array_ptr = (double *) buffer.ptr;
    for (int i = 0; i < buffer.shape[0]; i++) {
        for (int j = 0; j < buffer.shape[1]; j++) {
            array_ptr[i * buffer.shape[0] + j]++;
        }
    }

    // Return value is just to demonstrate how to return a numpy array
    // Incrementation is done in-place
    return numpy_array; 
}


double sum(pybind11::array_t<double> &numpy_array) {
    double sum = 0;
    
    auto array = numpy_array.unchecked<2>(); // Read-only
    for (int i = 0; i < array.shape(0); i++) {
        for (int j = 0; j < array.shape(0); j++) {
            sum += array(i, j);
        }
    }

    return sum;
}


PYBIND11_MODULE(module, m) {
    m.def("print_shape", &print_shape, pybind11::arg().noconvert());
    m.def("increment", &increment, pybind11::arg().noconvert());
    m.def("sum", &sum, pybind11::arg().noconvert());
}
