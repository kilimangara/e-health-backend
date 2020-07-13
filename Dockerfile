FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN usermod -a -G sudo root

RUN pip install pipenv

RUN apt-get update -qq \
  && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client

RUN mkdir /code
WORKDIR /code
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pipenv install

COPY . /code
