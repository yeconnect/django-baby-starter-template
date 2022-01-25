FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_code
WORKDIR /django_code
ADD requirements.txt /django_code/
RUN pip install -r requirements.txt
ADD . /django_code/