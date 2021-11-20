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
    packaging-dev \
    software-properties-common \
    tmux

RUN mkdir /databricks/python3/include; ln -s /usr/include/python3.8 /databricks/python3/include

RUN yes '' | add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    gcc-11 g++-11

RUN update-alternatives --remove-all cpp
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11 --slave /usr/bin/gcc-ar gcc-ar /usr/bin/gcc-ar-11 --slave /usr/bin/gcc-ranlib gcc-ranlib /usr/bin/gcc-ranlib-11  --slave /usr/bin/cpp cpp /usr/bin/cpp-11

RUN //databricks/python3/bin/pip3 install \
    check-manifest \
    cmake \
    flake8 \
    ninja \
    pybind11 \
    pytest \
    setuptools \
    setuptools-rust \
    tox

RUN wget -qO - https://sh.rustup.rs | sh -s -- --no-modify-path -y

ENV PATH="/root/.cargo/bin:/databricks/python3/bin:${PATH}"
