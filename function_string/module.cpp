#include <string>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <pybind11/pybind11.h>


std::string reverse_string(std::string sample_string) {
    std::reverse(sample_string.begin(), sample_string.end());

    return sample_string;
}

int count_digits(std::string sample_string) {
    int digit_count = 0;
    for (char c : sample_string) {
        if (std::isdigit(c)) {
            digit_count++;
        }
    }

    return digit_count;
}

PYBIND11_MODULE(module, m)
{
    m.def("reverse_string", &reverse_string);
    m.def("count_digits", &count_digits);
}
