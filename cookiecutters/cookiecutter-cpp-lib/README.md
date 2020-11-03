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
├───docs            # See below
│   ├───_build
│   ├───_static
│   └───_templates
├───example         # Self-contained example to test the compilation chain
├───include
│   └───myproject   # Header files
├───metadata        # See below
├───python
│   ├───pymyproject # Pybind11 bindings
│   └───tests       # Pytest unit tests of the bindings
├───src             # C++ source files
└───tests           # Catch2 unit tests
```

The `metadata/` subdirectory contains a few simple text files that hold the
metadata of the project

- `author.txt`
- `description.txt`: short description of the project
- `email.txt`
- `repository.txt`
- `version.txt`
- `year.txt`

These files can be updated any time. The changes should be reflected anywhere
relevant in the project, save for the `LICENSE` file, which is *never* altered
automatically. Note that the default library exposes two functions `author()`
and `version()` which return the author(s) and version number of the
library. These functions are statically compiled (they do not read the contents
of `author.txt` or `version.txt` at each call) but automatically updated when
the metadata files are modified.

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
