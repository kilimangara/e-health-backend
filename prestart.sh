#! /usr/bin/env bash

# # Let the DB start
#
# # Run migrations
sleep 8
alembic upgrade head
python /app/app/bin/backend_pre_start.py
#
# # Create initial data in DB
# python /app/app/initial_data.py
