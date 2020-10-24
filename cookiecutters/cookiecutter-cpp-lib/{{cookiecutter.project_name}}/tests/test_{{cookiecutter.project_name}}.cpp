#define _USE_MATH_DEFINES

#include "catch2/catch.hpp"
#include "{{cookiecutter.project_name}}/{{cookiecutter.project_name}}.hpp"

TEST_CASE("Test case #1") {
  SECTION("Section #1") {
    REQUIRE({{cookiecutter.project_name}}::author() == "{{cookiecutter.project_author}}");
    REQUIRE({{cookiecutter.project_name}}::version() == "{{cookiecutter.project_version}}");
    REQUIRE({{cookiecutter.project_name}}::return_one() == 1);
  }
}
