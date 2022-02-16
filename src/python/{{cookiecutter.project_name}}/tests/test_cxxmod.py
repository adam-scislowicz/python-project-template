import {{ cookiecutter.project_name }}.cxxmod


def test_aggregate():
    {{ cookiecutter.project_name }}.cxxmod.testing()

    a = {{ cookiecutter.project_name }}.cxxmod.ExampleClass()
    b = {{ cookiecutter.project_name }}.cxxmod.ExampleClass({"key": "val", "key2": "val2"})
    assert b.val == 4

    a.OverloadedMethod()
    a.OverloadedMethod(4)
    a.Method()
    assert a.val == 4
