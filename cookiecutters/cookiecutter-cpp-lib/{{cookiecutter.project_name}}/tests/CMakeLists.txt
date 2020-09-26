add_executable(test_{{cookiecutter.project_name}}
  test_{{cookiecutter.project_name}}_main.cpp
  test_{{cookiecutter.project_name}}.cpp
)

target_include_directories(test_{{cookiecutter.project_name}} PUBLIC ../include)

if (MATH_LIBRARY)
    target_link_libraries(test_{{cookiecutter.project_name}} ${MATH_LIBRARY})
endif ()

find_package(Catch2 REQUIRED)
target_link_libraries(test_{{cookiecutter.project_name}} PRIVATE {{cookiecutter.project_name}} Catch2::Catch2)

add_test(NAME test_{{cookiecutter.project_name}} COMMAND test_{{cookiecutter.project_name}})
