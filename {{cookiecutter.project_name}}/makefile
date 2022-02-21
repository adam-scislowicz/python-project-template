.PHONY: docker-image docker-interactive clean

docker-image: Dockerfile
	PROJECT_NAME="{{ cookiecutter.project_name }}" GID=$(shell id -g) DOCKER_BUILDKIT=1 docker build -f $< -t {{ cookiecutter.project_name }}:latest .

docker-interactive:
	docker run -v $(PWD):/home/$(USER)/{{ cookiecutter.project_name }} -it -w /home/$(USER)/{{ cookiecutter.project_name }} {{ cookiecutter.project_name }}:latest

clean:
	@rm -rf build* cmake-build* src/rust/target src/python/{{ cookiecutter.project_name }}.egg-info
