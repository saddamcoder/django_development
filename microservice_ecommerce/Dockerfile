FROM python:3.11.2
LABEL authors="sadda"

ENV PYTHONBUFFERED 1

WORKDIR /djangoapp

RUN apt-get update && apt-get install -y pkg-config


COPY . /djangoapp
COPY admin/requirements.txt /djangoapp/requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

CMD python admin/manage.py runserver 0.0.0.0:8000
