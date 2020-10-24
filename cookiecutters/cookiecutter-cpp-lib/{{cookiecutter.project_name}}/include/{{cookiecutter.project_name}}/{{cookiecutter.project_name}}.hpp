#pragma once

#if _WIN32
#define DllExport __declspec(dllexport)
#else
#define DllExport
#endif

#include <string>

namespace {{cookiecutter.project_name}}
{
  const std::string __author__ = "{{cookiecutter.project_author}}";

  DllExport std::string version();

  DllExport int return_one();
}  // namespace {{cookiecutter.project_name}}
