import pathlib

project = "{{cookiecutter.project_name}}"
copyright = "{{cookiecutter.project_year}}, {{cookiecutter.project_author}}"
author = "{{cookiecutter.project_author}}"
release = "{{cookiecutter.project_version}}"


extensions = ["sphinx.ext.todo", "breathe"]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

todo_include_todos = True

project_root = pathlib.Path.cwd().parent

breathe_projects_source = {
    "{{cookiecutter.project_name}}": (
        str(project_root / "include" / "{{cookiecutter.project_name}}"),
        ["{{cookiecutter.project_name}}.hpp"],
    )
}

breathe_doxygen_config_options = {"GENERATE_TODOLIST": "YES"}

html_theme = "alabaster"
html_static_path = ["_static"]
