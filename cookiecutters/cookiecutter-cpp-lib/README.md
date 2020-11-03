# cookiecutter-cpp-lib

A template for a full-featured C++ library.

- Compilation and installation through [Cmake](https://cmake.org)
- [Catch2](https://github.com/catchorg/Catch2) tests
- [Sphinx](http://www.sphinx-doc.org)+[Breathe](https://breathe.readthedocs.io) documentation
- [pybin11](https://pybind11.readthedocs.io) Python bindings

## Project generation

This template requires
[cookiecutter](https://cookiecutter.readthedocs.io/). Clone the `sbeculoos`
project, to e.g. `~/Documents/sbeculoos`

```
$ cd ~/Documents
$ git clone https://github.com/sbrisard/sbeculoos.git
```

To generate a new project, `cd` into the directory that will host it

```
$ cd /path/to/projects
$ cookiecutter /path/to/sbeculoos/cookiecutters/cookiecutter-cpp-lib
```

You will be asked a few questions. Then, a new subdirectory
`/path/to/projects/myproject` will be created, where `myproject` is the project
name that you have entered.

## Project layout

```
/path/to/projects/myproject
├───docs
│   ├───_build
│   ├───_static
│   └───_templates
├───example
├───include
│   └───myproject
├───metadata
├───python
│   ├───pymyproject
│   └───tests
├───src
└───tests
```

### The `metadata/` subdirectory

This directory contains a few simple text files that hold the metadata of the
project

- `author.txt`
- `description.txt`: short description of the project
- `email.txt`
- `repository.txt`
- `version.txt`
- `year.txt`

These files can be updated any time. The changes should be reflected anywhere
relevant in the project, save for the `LICENSE` file, which is *never* altered
automatically.

### The `include/myproject/` subdirectory

Holds the header files of the project.

### The `src/` subdirectory

Holds all `*.cpp` files. Note that the default file exposes two functions
`author()` and `version()` which return the author(s) and version number of the
library. These functions are statically compiled (they do not read the contents
of `author.txt` or `version.txt` at each call) but automatically updated when
the metadata files are modified.

### The `tests/` subdirectory

Holds the [Catch2](https://github.com/catchorg/Catch2) tests of the project.

### The `example/` subdirectory

Holds a very simple example that requires the library to build. This example
allows to check the overall installation.

### The `python/` subdirectory

Holds the [pybin11](https://pybind11.readthedocs.io) Python bindings and
[pytest](https://docs.pytest.org/) tests.

## Documentation

By default, the source files of the sphinx documentation are located in the
`docs/` subdirectory, and the HTML version is built in the `public/`
subdirectory. This layout is suitable for hosting the docs statically on GitLab
pages (for which an appropriate `gitlab-ci.yml` file is provided).

If you intend to host the documentation statically on GitHub, the `docs/`
subdirectory should be renamed to something else, and the HTML version should be
built in the `docs/` subdirectory. Note that you should put an empty `.nojekyll`
file in the `docs/` subdirectory for the documentation to be displayed
correctly.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
