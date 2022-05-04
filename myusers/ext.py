# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users System is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from . import config

from .modules import init_modules

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


class MyUsers(object):
    """MyUsers extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_modules(app)
        self.init_sentry(app)

        app.extensions["my-users"] = self

    def init_modules(self, app):
        """Flask modules initialization."""
        init_modules(app)

    def init_sentry(self, app):
        """Initialize the Sentry integration."""
        sentry_sdk.init(
            dsn=app.config["MY_USERS_SENTRY_DSN"],
            integrations=[FlaskIntegration()],
            traces_sample_rate=app.config["MY_USERS_SENTRY_SAMPLE_RATE"],
            # Extra tags
            release=app.config["MY_USERS_SENTRY_TAG_RELEASE"],
            environment=app.config["MY_USERS_SENTRY_TAG_ENVIRONMENT"],
        )

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("MY_USERS_") or k == "SQLALCHEMY_DATABASE_URI":
                app.config.setdefault(k, getattr(config, k))
