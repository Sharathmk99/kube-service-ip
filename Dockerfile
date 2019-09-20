FROM python:3.7.4-slim

LABEL maintainer="Sharath MK <sharathmk99@gmail.com>"

RUN apk update && apk upgrade && \
    apk add --no-cache git build-base ca-certificates

WORKDIR /workdir	
COPY . ./

RUN pip install kubernetes

CMD [ "python", "./main.py" ]