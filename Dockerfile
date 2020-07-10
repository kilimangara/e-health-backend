FROM python:3.6
RUN usermod -a -G sudo root

RUN pip install pipenv

RUN mkdir /code
WORKDIR /code
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pipenv install
COPY . /code
