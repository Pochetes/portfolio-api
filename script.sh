#!bin/bash

# prod Procfile
# gunicorn main:app --access-logfile - --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT

# dev
# pipenv run python main.py

# prod - Docker
gunicorn main:app --access-logfile - --worker-tmp-dir /dev/shm --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT