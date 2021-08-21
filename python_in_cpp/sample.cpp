#include <pybind11/embed.h>


void module_from_string() {
    pybind11::exec(R"(
        import numpy as np
        array = np.ones((10, 10))
        print("Shape: ", array.shape)
        print(f"Mean: {np.mean(array)}")
    )");
}


void module_import() {
    pybind11::module numpy = pybind11::module::import("numpy");
    pybind11::object array = numpy.attr("ones")(pybind11::make_tuple(10, 10));
    pybind11::print("Shape: ", array.attr("shape"));
    pybind11::print("Mean: ", numpy.attr("mean")(array));
}


int main() {
    pybind11::scoped_interpreter guard{};

    module_from_string();
    module_import();

    return 0;
}
