# pylint: skip-file

"""tests specific to cxxmod"""
import {{ cookiecutter.project_name }}.cxxmod


def test_aggregate() -> None:
    """all-in-one coverage motivated test for cxxmod."""
    {{ cookiecutter.project_name }}.cxxmod.testing()

    instance_a = {{ cookiecutter.project_name }}.cxxmod.ExampleClass()
    instance_b = {{ cookiecutter.project_name }}.cxxmod.ExampleClass({"key": "val", "key2": "val2"})
    assert instance_b.val == 4

    instance_a.OverloadedMethod()
    instance_a.OverloadedMethod(4)
    instance_a.Method()
    assert instance_a.val == 4
