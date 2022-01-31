FROM docker/python:3.9.10-slim-buster

COPY --chown=root:root . /tmp/noaa

WORKDIR /tmp/src

RUN pip install . && rm -rf /tmp/noaa