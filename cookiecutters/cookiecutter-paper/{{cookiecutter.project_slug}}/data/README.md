# The `data/` directory

Only data that is strictly necessary to reproduce the figures should be stored
in this repository. As such, the `data/` directory holds only small datasets
that can be stored in the following formats

- Small, tabular data files: `CSV` format. Use comment lines starting with `#`
  (at the beginning of the file) to describe the contents and all parameters
  that were used to produce de data.
- Medium-size, structured data: `JSON`.

All other file formats should be avoided. In particular, **binary** file formats
are ill-suited to versioning.

Larger datasets should be hosted elsewhere (e.g. [Zenodo](https://zenodo.org/)),
alongside scripts that perform extraction.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
