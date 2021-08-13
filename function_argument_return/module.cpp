#include <iostream>
#include <boost/python.hpp>


int count(int value) {
    int output_value = value;
    for (int i = 0; i < value; i++){
        output_value++;
    }

    return output_value;
}

BOOST_PYTHON_MODULE(module)
{
    boost::python::def(
        "count",
        count
    );
}
