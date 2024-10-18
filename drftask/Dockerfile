FROM python:3.11-slim

RUN mkdir /drf_app

WORKDIR /drf_app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#CMD python manage.py migrate