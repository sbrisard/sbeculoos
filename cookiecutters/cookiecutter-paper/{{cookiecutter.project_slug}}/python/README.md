# The `python/` directory

Scripts that *produce* data (simulations, etc.) should be distinct from scripts
that *consume* data to produce graphs. The rationale is that you should not need
to re-run a simulation if you need to alter a graph. So the typical workflow
should be

1. a first script saves some data in the `data/` directory,
2. a second script reads the data and saves the graphs in the `latex` directory.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
