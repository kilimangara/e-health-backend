FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app/

#RUN pip install pipenv sqlalchemy python-dotenv psycopg2-binary python-jose email-validator requests

RUN apt-get update -qq \
  && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
