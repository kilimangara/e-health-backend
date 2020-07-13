#! /usr/bin/env bash


# заходим в оболочку pipenv(.venv)
pipenv shell

# # Let the DB start
# python /app/app/backend_pre_start.py
#
# # Run migrations
alembic upgrade head
#
# # Create initial data in DB
# python /app/app/initial_data.py
