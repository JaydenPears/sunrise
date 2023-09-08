FROM python:3.10-slim


ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPYCACHEPREFIX=/tmp \
    POETRY_VIRTUALENVS_CREATE=false



RUN mkdir /app && \
    useradd -ms /bin/bash app && \
    chown -R app /app

WORKDIR /app

# dev dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl vim build-essential gettext libpq-dev libgraphviz-dev graphviz

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -U pip && \
    pip install -r /tmp/requirements.txt

USER app

