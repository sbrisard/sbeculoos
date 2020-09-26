# {{cookiecutter.project_name}} example

To build the example

```
cd ${PROJECT_ROOT}/example
mkdir build
cd build
cmake -D{{cookiecutter.project_name}}_DIR=${PATH/TO/{{cookiecutter.project_name}}-config.cmake} ..
cmake --build .
```
