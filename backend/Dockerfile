FROM python:3.7-alpine

COPY . .

RUN \ 
    pip install -r requirements.txt && \
    apk add make

CMD ["make", "local"]

