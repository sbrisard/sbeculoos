#pragma once

#if _WIN32
#define DllExport __declspec(dllexport)
#else
#define DllExport
#endif

#include <string>

namespace {{cookiecutter.project_name}} {

  const std::string __version__ = "{{cookiecutter.project_version}}";
  const std::string __author__ = "{{cookiecutter.project_author}}";

DllExport int return_one();

}