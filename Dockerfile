FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /project_arachnid

WORKDIR /project_arachnid

ADD . /project_arachnid

RUN pip install -r requirements.txt
