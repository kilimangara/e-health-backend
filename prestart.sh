#! /usr/bin/env bash

# # Let the DB start
# python /app/app/backend_pre_start.py
#
# # Run migrations
pipenv run alembic upgrade head
#
# # Create initial data in DB
# python /app/app/initial_data.py
