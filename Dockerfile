FROM python:3.9

# environment variables
ENV API_DIR /api

# installing pipenv library
RUN pip install pipenv

# setting the working directory
WORKDIR ${API_DIR}

# copying pipenv normal and hashed dependencies onto container 
COPY Pipfile Pipfile.lock ${API_DIR}/

# copying rest of application onto container
COPY ./ ${API_DIR}/

# installing dependencies directly to python distribution package on deploy mode 
RUN pipenv install --system --deploy

# starting api server
CMD ["pipenv", "run", "python", "main.py"]