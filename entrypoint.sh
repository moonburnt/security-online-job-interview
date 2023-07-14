#!/bin/bash

echo "Waiting for postgres to startup"
sleep 10
echo "Running migrations"
python backend/manage.py makemigrations
python backend/manage.py migrate

exec "$@"
