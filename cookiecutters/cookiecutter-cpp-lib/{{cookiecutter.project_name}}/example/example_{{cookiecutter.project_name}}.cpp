#include <iostream>
#include "{{cookiecutter.project_name}}/{{cookiecutter.project_name}}.hpp"

int main() {
  std::cout << "version = " << {{cookiecutter.project_name}}::__version__ << std::endl;
  std::cout << "author = " << {{cookiecutter.project_name}}::__author__ << std::endl;
  std::cout << "return_one() = " << {{cookiecutter.project_name}}::return_one() << std::endl;
  return 0;
}
