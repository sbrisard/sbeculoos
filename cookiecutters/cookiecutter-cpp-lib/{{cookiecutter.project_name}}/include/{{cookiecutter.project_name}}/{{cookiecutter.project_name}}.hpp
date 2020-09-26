#pragma once

#if _WIN32
#define DllExport __declspec(dllexport)
#else
#define DllExport
#endif

namespace {{cookiecutter.project_name}} {

DllExport int return_one();

}
