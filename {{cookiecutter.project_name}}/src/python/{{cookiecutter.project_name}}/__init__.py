"""Top-level package for {{ cookiecutter.project_name }}."""

import atexit

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


def shutdown():
    print("{{ cookiecutter.project_name }} module shutdown")


atexit.register(shutdown)

print("{{ cookiecutter.project_name }} module loaded.")
