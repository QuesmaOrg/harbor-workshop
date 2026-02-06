FROM ubuntu:26.04

RUN apt-get update && apt-get install -y \
    golang-go \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
COPY --chown=1000:1000 main.go /app

WORKDIR /app
