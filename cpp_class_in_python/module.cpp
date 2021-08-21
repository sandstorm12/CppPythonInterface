#include <string>
#include <iostream>
#include <pybind11/pybind11.h>


class Person {
    public:
        Person(const std::string &name, const int age) {
            _name = name;
            _age = age;
        }
        
        void set_name(const std::string &name) { 
            _name = name; 
        }
        
        const std::string &get_name() const { 
            return _name; 
        }

        void set_age(const int age) { 
            _age = age; 
        }
        
        const int &get_age() const { 
            return _age; 
        }

    private:
        std::string _name;
        int _age;
};

PYBIND11_MODULE(module, m)
{
    pybind11::class_<Person>(m, "Person")
        .def(pybind11::init<const std::string &, const int>())
        .def(
            "get_name", &Person::get_name
        )
        .def(
            "set_name", &Person::set_name
        )
        .def(
            "get_age", &Person::get_age
        )
        .def(
            "set_age", &Person::set_age
        );
}
