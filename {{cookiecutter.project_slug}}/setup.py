# pylint: skip-file

"""Setuptools based package definition for {{ cookiecutter.project_name }}"""

import os
import sys
import subprocess
import pathlib
import distutils.cmd

import setuptools
from setuptools import Extension
from setuptools.command.build_ext import build_ext
from setuptools_rust import Binding, RustExtension

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


class CmdClean(distutils.cmd.Command):
    """Cleanup files produced by the build process."""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call("make clean".split())


class CMakeExtension(Extension):
    """extension specialization for cmake integration"""

    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    """build_ext specialization for cmake"""

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cfg = "Debug" if self.debug else "Release"

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        cmake_args = [
            "-DPROJECT_DIR={}".format(pathlib.Path(__file__).parent.resolve()),
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={}".format(extdir),
            "-DPYTHON_EXECUTABLE={}".format(sys.executable),
            '-DVERSION="{{ cookiecutter.version }}"',
            "-DCMAKE_BUILD_TYPE={}".format(cfg),  # not used on MSVC, but no harm
        ]
        build_args = ["-v"]

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator:
                cmake_args += ["-GNinja"]

        else:

            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward compatibility
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}".format(cfg.upper(), extdir)]
                build_args += ["--config", cfg]

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or PyPA-build.
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += ["-j{}".format(self.parallel)]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(["cmake", "--build", "."] + build_args, cwd=self.build_temp)


long_description = (pathlib.Path(__file__).parent.resolve() / "README.md").read_text(
    encoding="utf-8"
)

setuptools.setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.repo_name }}",
    license="proprietary and confidential",
    license_files=("LICENSE.txt",),
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src/python"},
    packages=setuptools.find_packages(where="src/python"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    ext_modules=[CMakeExtension(name="{{ cookiecutter.project_slug }}.cxxmod")],
    cmdclass={"build_ext": CMakeBuild, "clean": CmdClean},
    rust_extensions=[
        RustExtension(
            "{{ cookiecutter.project_slug }}.rust_proj.rustmoda", path="src/rust/Cargo.toml", binding=Binding.PyO3
        )
    ],
    python_requires=">=3.6, <4",
    extras_require={
        "dev": ["check-manifest", "setuptools_rust"],
        "test": ["coverage"],
    },
    zip_safe=False,
)
