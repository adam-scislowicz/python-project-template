FROM databricksruntime/standard:9.x

ENV UID=1000
ENV GID=1000
ENV USER=ubuntu
ENV PROJECT_SLUG=project

WORKDIR /tmp
COPY requirements.txt .

LABEL maintainer="Adam Scislowicz <adam.scislowicz@gmail.com>"

SHELL ["/bin/bash", "-c"]

RUN apt-get clean \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    git \
    libfmt-dev \
    libpython3.8-dev \
    libspdlog-dev \
    ninja-build \
    packaging-dev \
    python3.8-venv \
    software-properties-common \
    tmux \
    && apt-get purge -y cmake \
    && mkdir /databricks/python3/include; ln -s /usr/include/python3.8 /databricks/python3/include \
    && wget -qO - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | apt-key add - &> /dev/null \
    && yes '' | apt-add-repository -y 'deb https://apt.kitware.com/ubuntu/ bionic main' \
    && yes '' | add-apt-repository -y ppa:ubuntu-toolchain-r/test \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    clang-format cmake gcc-11 g++-11 gdb \
    && update-alternatives --remove-all cpp \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11 --slave /usr/bin/gcc-ar gcc-ar /usr/bin/gcc-ar-11 --slave /usr/bin/gcc-ranlib gcc-ranlib /usr/bin/gcc-ranlib-11  --slave /usr/bin/cpp cpp /usr/bin/cpp-11 \
    && /databricks/python3/bin/pip3 install -r requirements.txt \
    && wget --progress=dot:giga https://github.com/danmar/cppcheck/archive/2.6.tar.gz \
    && tar xvzf 2.6.tar.gz \
    && mkdir cppcheck-2.6/build \
    && cd cppcheck-2.6/build \
    && cmake .. -GNinja \
    && ninja \
    && ninja install \
    && usermod -l $USER ubuntu \
    && usermod -u $UID $USER \
    && usermod -g $GID $USER \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER $USER

RUN mkdir -p /home/${USER}/${PROJECT_SLUG} \
    && wget -qO - https://sh.rustup.rs | sh -s -- --no-modify-path -y

ENV PATH="/home/${USER}/.cargo/bin:/databricks/python3/bin:${PATH}"

RUN rustup component add rustfmt clippy
