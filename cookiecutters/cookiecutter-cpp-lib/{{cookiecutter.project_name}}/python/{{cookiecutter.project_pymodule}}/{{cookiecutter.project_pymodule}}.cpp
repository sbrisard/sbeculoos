#include <pybind11/pybind11.h>

#include "{{cookiecutter.project_name}}/{{cookiecutter.project_name}}.hpp"

PYBIND11_MODULE({{cookiecutter.project_pymodule}}, m) {
  m.doc() = "Python bindings to the {{cookiecutter.project_name}} library";
  m.attr("__version__") = pybind11::cast({{cookiecutter.project_name}}::__version__);
  m.attr("__author__") = pybind11::cast({{cookiecutter.project_name}}::__author__);
  m.def("return_one", &{{cookiecutter.project_name}}::return_one, "Return one in all circumstances.");
}
