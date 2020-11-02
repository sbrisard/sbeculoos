# cookiecutter-cpp-lib

A template for a full-featured C++ library.

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
