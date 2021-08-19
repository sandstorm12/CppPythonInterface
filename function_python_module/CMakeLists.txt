cmake_minimum_required(VERSION 3.5)

project(CppPythonInterface)

find_package(PythonLibs 3.8 REQUIRED)
find_package(Boost COMPONENTS python COMPONENTS numpy REQUIRED)

set(CMAKE_SHARED_MODULE_PREFIX "")

add_executable(module.out module.cpp)

target_link_libraries(module.out ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_include_directories(module.out PRIVATE ${PYTHON_INCLUDE_DIRS})
