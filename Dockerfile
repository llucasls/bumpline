ARG PYTHON_IMAGE=python
ARG PYTHON_VERSION=latest
FROM ${PYTHON_IMAGE}:${PYTHON_VERSION}

WORKDIR /app

COPY . .

ENTRYPOINT ["/app/entrypoint.py"]
