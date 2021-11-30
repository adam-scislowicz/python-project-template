.PHONY: beautify lint build-dev build

beautify:
	black .

	@find ./src -regex '\(.*\.cpp\|.*\.h\)' -exec bash -c "echo clang-format -i {}... && clang-format -i {}" \;

	(cd ./src/rust && cargo fmt)

lint:
	flake8

	# XXXADS TODO: clang-tidy

	(cd ./src/rust && cargo clippy)

build-dev:
	pip install -e . -vvv

build:
	pip install . -vvv