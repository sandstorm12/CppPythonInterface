cmake_minimum_required(VERSION 3.5)

project(CppPythonInterface)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

pybind11_add_module(module SHARED module.cpp)
