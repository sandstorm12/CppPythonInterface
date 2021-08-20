#include <iostream>
#include <pybind11/pybind11.h>


int sum(pybind11::dict &input_dict) {
    int sum = 0;
    for (auto item : input_dict) {
        sum += pybind11::cast<int>(item.second);
    }
    
    return 0;
}


void increment(pybind11::dict &input_dict) {
    for (auto item : input_dict) {
        input_dict[item.first] = pybind11::cast<int>(item.second) + 1;
    }
}


int max(pybind11::dict &input_dict) {
    int max = 0;
    for (auto item : input_dict) {
        if (pybind11::cast<int>(item.second) > max) {
            max = pybind11::cast<int>(item.second);
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
