FROM python:3.7.4-slim

LABEL maintainer="Sharath MK <sharathmk99@gmail.com>"

WORKDIR /workdir	
COPY . ./

RUN pip install kubernetes

ENTRYPOINT [ "python", "./main.py" ]