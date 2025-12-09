cmake_minimum_required(VERSION 3.15)
project(mylib LANGUAGES CXX)

add_library(mylib src/hello.cpp)
target_include_directories(mylib PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:include>
)
target_compile_features(mylib PUBLIC cxx_std_17)
set_target_properties(mylib PROPERTIES PUBLIC_HEADER "src/hello.h")