cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

set(CMAKE_CXX_FLAGS "-std=c++17 -g -O3 -m64 -lstdc++ -fopenmp -fPIC -fpermissive")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

project(CSR_solver)

file(GLOB SOURCES
    include/*.h
    lib/*.cpp
)

add_definitions(-DEIGEN_MALLOC_ALREADY_ALIGNED=0)
add_executable(test_solver CSR_test.cpp ${SOURCES})
target_include_directories(UDL_SPS_v3.00 PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")
