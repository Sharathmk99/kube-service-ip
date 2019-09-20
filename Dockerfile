FROM python:3

LABEL maintainer="Sharath MK <sharathmk99@gmail.com>"

WORKDIR /workdir	
COPY . ./

RUN pip install kubernetes

ENTRYPOINT [ "python", "main.py" ]