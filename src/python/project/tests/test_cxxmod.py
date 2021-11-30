import project.cxxmod


def test_aggregate():
    project.cxxmod.testing()

    a = project.cxxmod.ExampleClass()
    b = project.cxxmod.ExampleClass({"key": "val", "key2": "val2"})
    assert b.val == 4

    a.OverloadedMethod()
    a.OverloadedMethod(4)
    a.Method()
    assert a.val == 4
