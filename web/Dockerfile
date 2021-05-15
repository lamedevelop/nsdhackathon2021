FROM python:3.7-alpine

COPY ./requirements.txt /tmp/requirements.txt

RUN \
    apk add --no-cache make && \
    pip install -r /tmp/requirements.txt

COPY . /etc/web/

WORKDIR /etc/web/

CMD ["make", "local"]

