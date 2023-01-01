FROM python:3.11.1-buster as builder

COPY --chown=root:root . /tmp/noaa
WORKDIR /tmp/noaa

RUN pip wheel --use-pep517 .

FROM python:3.11.1-buster

COPY --from=builder /tmp/noaa/*.whl /tmp

RUN cd /tmp && pip install *.whl && rm *.whl