# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import os
from .version import __version__ as package_version

#
# Sentry DSN
#
MY_USERS_SENTRY_DSN = os.getenv("MY_USERS_SENTRY_DSN", None)  # nqa

MY_USERS_SENTRY_TAG_RELEASE = os.getenv("MY_USERS_SENTRY_TAG_RELEASE", None)  # nqa

MY_USERS_SENTRY_TAG_ENVIRONMENT = os.getenv(
    "MY_USERS_SENTRY_TAG_ENVIRONMENT", package_version  # nqa
)

MY_USERS_SENTRY_SAMPLE_RATE = os.getenv("MY_USERS_SENTRY_SAMPLE_RATE", 1.0)  # nqa

#
# Database
#
SQLALCHEMY_DATABASE_URI = os.getenv(
    "MY_USERS_SENTRY_DB_URI", "sqlite:///:memory:"
)  # nqa
