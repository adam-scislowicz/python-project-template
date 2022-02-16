.PHONY: docker-image docker-interactive clean

docker-image: Dockerfile
	DOCKER_BUILDKIT=1 docker build . -f $< -t conda-forge-template:latest /bin/bash

docker-interactive:
	docker run -v $(PWD):/home/ubuntu -it -w /home/ubuntu conda-forge-template:latest

clean:
	@rm -rf build* cmake-build* src/rust/target src/python/{{ cookiecutter.project_name }}.egg-info
