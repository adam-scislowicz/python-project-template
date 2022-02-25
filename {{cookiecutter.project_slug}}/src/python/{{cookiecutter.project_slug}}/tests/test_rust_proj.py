# pylint: skip-file

"""tests specific to rust_proj"""
import {{ cookiecutter.project_slug }}.rust_proj.rustmoda


def test_aggregate() -> None:
    """all-in-one coverage motivated test for rust_proj."""
    {{ cookiecutter.project_slug }}.rust_proj.rustmoda.testing()
