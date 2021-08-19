#include <iostream>
#include <boost/python.hpp>


void increment(boost::python::dict &value) {
    boost::python::list keys = value.keys();
    for (int i = 0; i < len(keys); ++i) {
        value[keys[i]] += 1;
    }
}

BOOST_PYTHON_MODULE(module)
{
    boost::python::def(
        "increment",
        increment
    );
}
