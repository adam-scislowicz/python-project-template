FROM databricksruntime/standard:9.x

LABEL maintainer="Adam Scislowicz <adam.scislowicz@gmail.com>"

RUN apt-get clean
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    git \
    libfmt-dev \
    libpython3.8-dev \
    libspdlog-dev \
    ninja-build \
    packaging-dev \
    python3.8-venv \
    software-properties-common \
    tmux

RUN apt-get purge -y cmake

RUN mkdir /databricks/python3/include; ln -s /usr/include/python3.8 /databricks/python3/include

RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | sudo apt-key add -
RUN yes '' | apt-add-repository -y 'deb https://apt.kitware.com/ubuntu/ bionic main'

RUN yes '' | add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    clang-format cmake gcc-11 g++-11 gdb

RUN update-alternatives --remove-all cpp
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11 --slave /usr/bin/gcc-ar gcc-ar /usr/bin/gcc-ar-11 --slave /usr/bin/gcc-ranlib gcc-ranlib /usr/bin/gcc-ranlib-11  --slave /usr/bin/cpp cpp /usr/bin/cpp-11

RUN /databricks/python3/bin/pip3 install \
    black \
    check-manifest \
    cookiecutter \
    flake8 \
    nox \
    pre-commit \
    pybind11 \
    pytest \
    pyyaml \
    setuptools \
    setuptools-rust

RUN wget https://github.com/danmar/cppcheck/archive/2.6.tar.gz
RUN tar xvzf 2.6.tar.gz && \
    mkdir cppcheck-2.6/build && \
    cd cppcheck-2.6/build && \
    cmake .. -GNinja && \
    ninja && \
    ninja install

RUN wget -qO - https://sh.rustup.rs | sh -s -- --no-modify-path -y

ENV PATH="/root/.cargo/bin:/databricks/python3/bin:${PATH}"

RUN rustup component add rustfmt clippy
