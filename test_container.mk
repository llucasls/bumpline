PYTHON_IMAGE   = python
PYTHON_VERSION = latest

test: clean
	PYTHON_IMAGE=$(PYTHON_IMAGE); export PYTHON_IMAGE
	PYTHON_VERSION=$(PYTHON_VERSION); export PYTHON_VERSION
	if test -t 1; then
		printf "\n\n"
		echo "$(PYTHON_IMAGE):$(PYTHON_VERSION)"
		docker-compose up --exit-code-from test
	else
		docker-compose -f no-tty.yml up --exit-code-from test
	fi
	docker-compose down

clean:
	if test -n "$$(docker container ls -a -f name=test -q)"; then
		docker-compose down
	fi
	if test -n "$$(docker image ls -f reference=bumpline-test -q)"; then
		docker image rm bumpline-test
	fi

.PHONY: test clean

.SILENT:

.ONESHELL:
