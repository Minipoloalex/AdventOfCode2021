cmake_minimum_required(VERSION 3.23)
project(2021_Day_15)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")


add_executable(Day_15 main.cpp Position.cpp Position.h types.h)
