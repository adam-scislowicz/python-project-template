.PHONY: beautify build-dev build

beautify:
	black .

	@find ./src -regex '\(.*\.cpp\|.*\.h\)' -exec bash -c "echo clang-format -i {}... && clang-format -i {}" \;

build-dev:
	pip install -e . -vvv

build:
	pip install . -vvv