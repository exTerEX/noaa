FROM python:3.10.2-slim-buster

COPY --chown=root:root . /tmp/noaa

WORKDIR /tmp/noaa

# FIXME: Feed version in some way?
#RUN pip install . && rm -rf /tmp/noaa