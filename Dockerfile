FROM python:3.10.7-buster as builder

COPY --chown=root:root . /tmp/noaa
WORKDIR /tmp/noaa

RUN pip wheel --use-pep517 .

FROM python:3.10.7-buster

COPY --from=builder /tmp/noaa/*.whl /tmp

RUN cd /tmp && pip install *.whl && rm *.whl