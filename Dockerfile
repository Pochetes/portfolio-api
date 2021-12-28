FROM python:3.9

# environment variables
ENV API_DIR /api

# installing pipenv library
RUN pip3 install pipenv

# setting the working directory
WORKDIR ${API_DIR}

# copying pipenv normal and hashed dependencies onto container 
COPY Pipfile ${API_DIR}/ 
COPY Pipfile.lock ${API_DIR}/

# installing dependencies directly to python distribution package on deploy mode 
RUN set -ex && pipenv install --system --deploy

# copying rest of application onto container
COPY ./ ${API_DIR}/

RUN useradd -m rob
USER rob

CMD [ "/bin/bash", "script.sh" ]