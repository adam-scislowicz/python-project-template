.PHONY: docker-image docker-interactive clean

docker-image: Dockerfile
	DOCKER_BUILDKIT=1 docker build -f $< -t python-project-template:latest .

docker-interactive:
	docker run -v $(PWD):/home/ubuntu -it -w /home/ubuntu python-project-template:latest

clean:
	@rm -rf build* cmake-build* src/rust/target src/python/{{ cookiecutter.project_name }}.egg-info
