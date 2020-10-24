mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=C:\opt\{{cookiecutter.project_name}} ..
cmake --build . --config Release
cmake --install . --config Release
