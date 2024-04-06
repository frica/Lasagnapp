# syntax=docker/dockerfile:1
FROM zauberzeug/nicegui:1.4.20

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app