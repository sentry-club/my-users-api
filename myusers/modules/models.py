# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users System is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """Super simple User class model."""

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80))
    username = db.Column(db.String(80))

    email = db.Column(db.String(120))

    def to_dict(self):
        """Transform object to dict."""
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
        }


def init_module(app):
    """Factory function to initialize the models module."""

    db.init_app(app)
