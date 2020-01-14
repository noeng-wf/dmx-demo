cmake_minimum_required(VERSION 3.1)
project(hello-cpp)
add_executable(hello-cpp hello.cpp)
install(TARGETS hello-cpp DESTINATION bin)
