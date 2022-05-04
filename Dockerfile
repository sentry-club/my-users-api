# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

FROM python:3.8-slim-buster

EXPOSE 5000
ENV MY_USERS_SENTRY_DB_URI sqlite:////app/database.db

RUN apt-get update -y \
    && apt-get install -y git make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/src

COPY . .
RUN pip install \
    poetry \
    gunicorn \
    && poetry config virtualenvs.create false \
    && poetry install

# generating dummy data (only for tests purposes.)
RUN myusers database createdb \
    && myusers database populatedb

CMD ["gunicorn", "-w4", "--bind=0.0.0.0:5000", "myusers.cli:create_app_wsgi()"]
