************
Installation
************


Installing the C++ library
==========================

This is a CMake_ based project. The installation procedure is standard. First,
clone the repository. Then, ``cd`` into the root directory of the
{{cookiecutter.project_name}} project. Let
``{{cookiecutter.project_name}}_INSTALL_PREFIX`` be the path to the directory
where {{cookiecutter.project_name}} should be installed::

  $ git clone {{cookiecutter.project_repository}}
  $ cd {{cookiecutter.project_name}}
  $ mkdir build
  $ cd build
  $ cmake -DCMAKE_INSTALL_PREFIX={{cookiecutter.project_name}}_INSTALL_PREFIX ..
  $ cmake --build . --config Release
  $ cmake --install . --config Release

.. note:: The ``--config`` option might not be available, depending on the
   selected generator.

At this point, {{cookiecutter.project_name}} should be installed. You can now
run the tests::

  $ ctest . -C Release

.. note:: Depending on the system, you might need to add
   ``{{cookiecutter.project_name}}_INSTALL_PREFIX`` to your ``PATH`` environment
   variable.


Compiling your first {{cookiecutter.project_name}} program
==========================================================

``cd`` into the ``example`` subdirectory. The provided example program should be
compiled and linked against {{cookiecutter.project_name}}::

  $ mkdir build
  $ cd build
  $ cmake -D{{cookiecutter.project_name}}_DIR={{cookiecutter.project_name}}_INSTALL_PREFIX/lib/cmake/{{cookiecutter.project_name}} ..
  $ cmake --build . --config Release

An executable called ``example_{{cookiecutter.project_name}}`` should be present
in the ``build/Release`` subdirectory.


.. _CMake: https://cmake.org/
