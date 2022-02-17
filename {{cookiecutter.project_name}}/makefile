.PHONY: docker-image docker-interactive clean

docker-image: Dockerfile
	DOCKER_BUILDKIT=1 docker build -f $< -t {{ cookiecutter.project_name }}:latest .

docker-interactive:
	docker run -v $(PWD):/home/ubuntu/host -it -w /home/ubuntu/host {{ cookiecutter.project_name }}:latest

clean:
	@rm -rf build* cmake-build* src/rust/target src/python/{{ cookiecutter.project_name }}.egg-info
