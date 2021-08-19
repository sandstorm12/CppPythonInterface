#include <boost/python.hpp>
#include "boost/shared_ptr.hpp"
#include "boost/python/stl_iterator.hpp"


template<typename T>
inline
std::vector< T > py_list_to_std_vector(
        const boost::python::object& iterable ) {
    return std::vector<T> (
        boost::python::stl_input_iterator<T>(iterable),
        boost::python::stl_input_iterator<T>()
    );
}


template <class T>
inline
boost::python::list std_vector_to_py_list(std::vector<T> vector) {
    typename std::vector<T>::iterator iter;
    
    boost::python::list list;
    for (iter = vector.begin(); iter != vector.end(); ++iter) {
        list.append(*iter);
    }
    
    return list;
}


boost::python::list reverse(const boost::python::object list) {
    std::vector<int> output_vector = py_list_to_std_vector<int>(list);
    std::reverse(output_vector.begin(), output_vector.end());
    boost::python::list output_list = std_vector_to_py_list(output_vector);

    return output_list;
}

BOOST_PYTHON_MODULE(module) {
    boost::python::def(
        "reverse",
        reverse
    );
}
