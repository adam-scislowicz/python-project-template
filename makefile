.PHONY: beautify lint build-dev build clean

beautify:
	black .

	@find ./src -regex '\(.*\.cpp\|.*\.h\)' -exec bash -c "echo clang-format -i {}... && clang-format -i {}" \;

	(cd ./src/rust && cargo fmt)

lint:
	flake8

	cppcheck --enable=warning,performance,portability,information,missingInclude \
		-I/databricks/python3/lib/python3.8/site-packages/pybind11/include/ \
		--suppress=preprocessorErrorDirective:/databricks/python3/lib/python3.8/site-packages/pybind11/include/pybind11/detail/common.h \
		--std=c++20 \
		-UVERSION_INFO \
		--check-config \
		./src/cxx

	(cd ./src/rust && cargo clippy)

build-dev:
	pip install -e . -vvv

build:
	pip install . -vvv

clean:
	@rm -rf build* cmake-build*