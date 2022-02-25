"""Top-level package for {{ cookiecutter.project_slug }}."""

import atexit

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


def shutdown() -> None:
    """This function is called on module exit."""

    print("{{ cookiecutter.project_slug }} module shutdown")


atexit.register(shutdown)

print("{{ cookiecutter.project_slug }} module loaded.")
