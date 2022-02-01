FROM python:3.10.2-slim-buster

COPY --chown=root:root . /tmp/noaa

WORKDIR /tmp/noaa

RUN pip install . && rm -rf /tmp/noaa