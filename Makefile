.PHONY: flake clean build down upn upc test

flake:
	@echo "*** Linting python code ***"
	flake8 . --ignore="E501"

clean:
	@echo "*** Cleaning the repo ***"
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -name .ipynb_checkpoints`

build: clean
	@echo "*** Rebuilding images for docker compose container collections ***"
	docker-compose -f ./docker-compose-notebook.yml build
	docker-compose -f ./docker-compose-cluster.yml build

down:
	@echo "*** Stopping spark servers ***"
	docker-compose -f ./docker-compose-notebook.yml down --remove-orphans
	docker-compose -f ./docker-compose-cluster.yml down --remove-orphans

upn: down
	@echo "*** Starting spark notebook server ***"
	docker-compose -f ./docker-compose-notebook.yml up -d

upc: down
	@echo "*** Starting spark cluster server ***"
	docker-compose -f ./docker-compose-cluster.yml up -d

test: build
	@echo "*** Running tests ***"
	make upn
	./bin/test
	make down
