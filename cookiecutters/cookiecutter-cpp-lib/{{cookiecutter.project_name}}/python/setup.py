import configparser
import os.path

import pybind11
import setuptools

if __name__ == "__main__":
    metadata = {
        "name": "{{cookiecutter.project_pymodule}}",
        "version": "version",
        "author": "author",
        "author_email": "author_email",
        "description": "description",
        "url": "url",
    }

    with open(os.path.join("..", "README.md"), "r") as f:
        metadata["long_description"] = f.read()

    config = configparser.ConfigParser()
    config.read("setup.cfg")
    {{cookiecutter.project_name}}_include_dir = config["{{cookiecutter.project_name}}"].get("include_dir", "")
    {{cookiecutter.project_name}}_library_dir = config["{{cookiecutter.project_name}}"].get("library_dir", "")

    {{cookiecutter.project_pymodule}} = setuptools.Extension(
        "{{cookiecutter.project_pymodule}}.{{cookiecutter.project_pymodule}}",
        include_dirs=[pybind11.get_include(),
                      {{cookiecutter.project_name}}_include_dir],
        sources=[os.path.join("{{cookiecutter.project_pymodule}}",
                              "{{cookiecutter.project_pymodule}}.cpp")],
        libraries=["{{cookiecutter.project_name}}"],
        library_dirs=[{{cookiecutter.project_name}}_library_dir],
    )

    setuptools.setup(
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        ext_modules=[{{cookiecutter.project_pymodule}}],
        **metadata
    )
