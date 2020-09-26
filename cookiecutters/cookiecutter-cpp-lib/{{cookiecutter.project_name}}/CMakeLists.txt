cmake_minimum_required(VERSION 3.13)
project(
  {{cookiecutter.project_name}}
  VERSION {{cookiecutter.project_version}}
  DESCRIPTION "{{cookiecutter.project_description}}"
  LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
include(CTest)

add_subdirectory(include)
add_subdirectory(src)
add_subdirectory(tests)
