# A sample pypi and conda-forge package.

This sample package is meant to represent engineering best-practices. It
includes python code along with both c++ and rust back-end code,
each accessible via python bindings.

A Dockerfile is included to allow for reproducable builds of the package.

Automatic code formatting, standards compliance validation, unit tests
, performance benchmarking, and python version compatibility testing
is included using tox.

Code beautification is accomplished as follows:
  1) python code is beautified using block
  2) c++ code is beautified using clang-format
  3) rust code is beautified using cargo fmt

Linting is accomplished using the follows:
  1) package specification are validates using check-manifest
  2) setup.py is validated using python check -m -s
  3) python code is validated using flake8
  4) c++ code is validated using cppcheck
  5) rust code is validated using cargo clippy

Unit tests are accomplished using py.test.

Benchmarks use pytest-benchmark.
