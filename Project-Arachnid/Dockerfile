# Pull the base image
FROM python:3.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
#Upgrade pip
RUN pip install pip -U
ADD requirements.txt /app/
#Install dependencies
RUN pip install -r requirements.txt
ADD . /app/

# Install python3 database connector for mysql
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y

