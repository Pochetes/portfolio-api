#!bin/bash

# dev
# pipenv run python main.py

# prod
gunicorn main:app --access-logfile - --worker-tmp-dir /dev/shm --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080