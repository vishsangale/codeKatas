cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

set(NAME codeKatas)
project(${NAME})


add_executable(${NAME} example.cpp)

set_property(TARGET ${NAME} PROPERTY CXX_STANDARD 17)
