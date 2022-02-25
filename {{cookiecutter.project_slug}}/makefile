.PHONY: docker-image docker-interactive clean

docker-image: Dockerfile
	PROJECT_SLUG="{{ cookiecutter.project_slug }}" GID=$(shell id -g) DOCKER_BUILDKIT=1 docker build -f $< -t {{ cookiecutter.project_slug }}:latest .

docker-interactive:
	docker run -v $(PWD):/home/$(USER)/{{ cookiecutter.project_slug }} -it -w /home/$(USER)/{{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}:latest

clean:
	@rm -rf build* cmake-build* src/rust/target src/python/{{ cookiecutter.project_slug }}.egg-info
