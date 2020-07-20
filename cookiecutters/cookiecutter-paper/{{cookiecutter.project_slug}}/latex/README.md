# The `latex/` directory

Here are guidelines for the organization of the LaTeX source files. These
guidelines are important. Following them will make the submission process much
easier.

All files should be stored in a flat directory structure. In other words, the
`*.tex`, `*.bib` and `*.pdf` (figures) files should all be stored at the root of
the `latex/` directory (no subdirectories).

The `latex/` subdirectory should be self-contained, meaning that compilation of
the paper should require no files outside the `latex/` subdirectory.

**DO NOT COMMIT TO GIT THE PDF VERSION OF YOUR PAPER.** If you rename the latex
file, please update the `./.gitignore` file accordingly.

Committing the PDF version of the figures is fine, as it facilitates compilation
of the paper (without first reruning the plotting scripts). Besides, these files
should not change too often.

## Style guide

Until we decide which journal to submit to, we will use Elsevier's templates
(see
[documentation](https://www.elsevier.com/authors/author-schemas/latex-instructions)).

We will also use the AMS packages extensively (see
[documentation](https://ctan.crest.fr/tex-archive/macros/latex/required/amsmath/amsldoc.pdf)). **DO NOT USE THE** `\eqnarray` **ENVIRONMENT!**

In general, use extra packages only if absolutely necessary.

Use a blank line, rather than `\\\\`, to separate two paragraphs.

Do not use placement specifiers for figures (trust LaTeX!). These specifiers
will be ignored by the journal editor anyway.

In general, avoid manual formatting of text (such as `\textsc{fgure}`). Manual
formatting usually conflicts with the journal stylesheet (and is removed by the
editor).

Use indices and exponents very sparingly!

Some default macros are provided in the `LaTeX` source file. In particular

- `\D` should be used for the differential element, e.g. `\D V` for a volume
  element,
- `\vec` is used for vectors,
- `\tens` is used for tensors, regardless of their order.

Currently, the same typeface is used for vectors and tensors. We usually do not
use different notations for tensors of different orders, as the order is usually
pretty clear from the context.

The classical differential operators are written in full letters. Use the
macros: `\grad`, `\div` and `\curl`.

All equations should be numbered, even if they are not cited. These facilitates
the review process.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
