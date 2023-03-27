ARG PYTHON_VERSION=latest
FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

ENTRYPOINT ["/app/entrypoint.py"]
