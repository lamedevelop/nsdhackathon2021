FROM python:3.7-alpine

ENV FLASK_APP=main

COPY requirements.txt .

RUN \ 
    pip install -r requirements.txt

WORKDIR /tmp

COPY ./templates templates
COPY main.py .

CMD ["flask", "run", "--host", "0.0.0.0"]

