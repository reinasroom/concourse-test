FROM alpine:latest

ENV GID=10001
ENV UID=10001
ENV USER=fly

RUN addgroup -g $GID "$USER" && adduser --disabled-password --home "/home/$USER" -G "$USER" --uid $UID "$USER"

RUN apk update && apk upgrade --no-cache && apk add curl postgresql-client

RUN cd /usr/local/bin/ && curl -L "https://github.com/concourse/concourse/releases/download/v7.9.1/fly-7.9.1-linux-amd64.tgz" | tar xvz && apk del curl

WORKDIR /home/fly

ENTRYPOINT ["/usr/local/bin/fly"]
