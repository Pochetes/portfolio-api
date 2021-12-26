FROM python:3.9

WORKDIR /api

EXPOSE 8080

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./ /api

CMD ["python", "main.py"]