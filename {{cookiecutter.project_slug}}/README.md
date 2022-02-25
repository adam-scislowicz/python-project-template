# A python project template supporting pypi and conda-forge packaging.

This package template is meant to represent best-practices. It
includes python code along with both c++ and rust back-end code,
each accessible via python bindings.

A Dockerfile is included to allow for reproducable builds of the package.

Automatic code formatting, standards compliance validation, unit tests,
 performance benchmarking, and python version compatibility testing
is included using nox and pre-commit.

Unit tests are accomplished using py.test.

Benchmarks use pytest-benchmark.

##  Basic Usage

  * make docker-image
  * make docker-interactive
    * nox # to run all nox sessions
    * or to run a specific nox session:
      * nox -s lint
      * nox -s tests

## TODO

  1) replace the pre-commit system commands using bash with ones using python
  2) replace the two bash scripts in packaging/conda with python scripts for better platform portability
