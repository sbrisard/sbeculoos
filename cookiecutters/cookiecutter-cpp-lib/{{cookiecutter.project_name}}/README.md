# {{cookiecutter.project_name}}

## Installation

This project uses the [CMake](https://cmake.org/) build tool. `cd` into the
project directory

```
md build
cd build
cmake -DCMAKE_INSTALL_PREFIX="C:\opt\{{cookiecutter.project_name}}" ..
cmake --build .
cmake --intall .
```

If relevant (e.g. for the MSVC compiler suite), you can specify the build
configuration

```
cmake --config Release --build .
cmake --config Release --install .
```

To run the tests

```
ctest .
```

or

```
ctest -C Release .
```

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->