FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app/

RUN pip install pipenv

RUN apt-get update -qq \
  && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client

COPY Pipfile /app/Pipfile
RUN pipenv install

COPY . /app
