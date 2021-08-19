#include <iostream>
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>


float mean(boost::python::numpy::ndarray &input_array) {
    float mean_value = boost::python::extract<float>(input_array.attr("mean")());

    return mean_value;
}

BOOST_PYTHON_MODULE(module)
{
    boost::python::numpy::initialize();

    boost::python::def(
        "mean",
        mean
    );

    boost::python::def(
        "mean_loop",
        mean_loop
    );
}
