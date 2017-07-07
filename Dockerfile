FROM alpine:3.4
MAINTAINER Dan Bugnar <dan_bugnar@yahoo.com>

RUN apk --update add --no-cache bash python3 docker openssh-client build-base libffi-dev openssl openssl-dev python3-dev tar curl && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

WORKDIR /usr/src/api

COPY . /usr/src/api
RUN pip3 install -r requirements.txt && \
	rm -rf requirements.txt



CMD [ "python3", "./app.py" ]
EXPOSE 12344