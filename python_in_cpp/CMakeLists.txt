cmake_minimum_required(VERSION 3.5)

project(CppPythonInterface)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O2")

add_executable(sample.out sample.cpp)
target_link_libraries(sample.out PRIVATE pybind11::embed)
