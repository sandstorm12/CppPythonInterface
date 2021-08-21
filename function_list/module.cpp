#include <iostream>
#include <pybind11/pybind11.h>


int sum(pybind11::list &input_list) {
    int sum = 0;
    for (auto item : input_list) {
        sum += pybind11::cast<int>(item);
    }
    
    return sum;
}


void increment(pybind11::list &input_list) {
    for (int i = 0; i < int(input_list.size()); i++) {
        input_list[i] = pybind11::cast<int>(input_list[i]) + 1;
    }
}


int max(pybind11::list &input_list) {
    int max = 0;
    for (auto item : input_list) {
        if (pybind11::cast<int>(item) > max) {
            max = pybind11::cast<int>(item);
        }
    }

    return max;
}


PYBIND11_MODULE(module, m)
{
    m.def("sum", &sum);
    m.def("increment", &increment);
    m.def("max", &max);
}
