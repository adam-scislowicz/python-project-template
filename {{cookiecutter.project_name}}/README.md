# A sample pypi and conda-forge package.

This sample package is meant to represent engineering best-practices. It
includes python code along with both c++ and rust back-end code,
each accessible via python bindings.

A Dockerfile is included to allow for reproducable builds of the package.

Automatic code formatting, standards compliance validation, unit tests
, performance benchmarking, and python version compatibility testing
is included using nox.

Code beautification is accomplished as follows:
  1) python code is beautified using block
  2) c++ code is beautified using clang-format
  3) rust code is beautified using cargo fmt

Unit tests are accomplished using py.test.

Benchmarks use pytest-benchmark.

##  Basic Usage

  * cookiecutter <repo>
  * cd <project_name>
  * make docker-image
  * make docker-interactive
    * nox
    * or
      * nox -s lint
      * nox -s tests

## TODO

  1) replace the makefile with additional noxfile sessions
  2) replace the pre-commit system commands using bash with ones using python
  3) replace the two bash scripts in packaging/conda with python scripts for better platform portability
