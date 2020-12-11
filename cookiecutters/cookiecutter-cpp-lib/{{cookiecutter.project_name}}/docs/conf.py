import pathlib

project_root = pathlib.Path.cwd().parent


def get_metadata(key):
    with open(project_root / "metadata" / (key + ".txt"), "r", encoding="utf8") as f:
        return f.read()


project = "{{cookiecutter.project_name}}"
copyright = get_metadata("year") + ", " + get_metadata("author")
author = get_metadata("author")
release = get_metadata("version")


extensions = ["sphinx.ext.autodoc", "sphinx.ext.todo", "breathe"]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

todo_include_todos = True


breathe_projects_source = {
    "{{cookiecutter.project_name}}": (
        str(project_root / "include" / "{{cookiecutter.project_name}}"),
        ["{{cookiecutter.project_name}}.hpp"],
    )
}

breathe_doxygen_config_options = {"GENERATE_TODOLIST": "YES"}

html_theme = "alabaster"
html_static_path = ["_static"]
