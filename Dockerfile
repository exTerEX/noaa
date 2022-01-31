FROM python:3.9.10-slim-buster

COPY --chown=root:root . /tmp/noaa

WORKDIR /tmp/noaa

RUN pip install . && rm -rf /tmp/noaa