# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import click

from flask import Flask
from flask.cli import FlaskGroup, with_appcontext

from faker import Faker

from .ext import MyUsers
from .modules.models import User, db as db_module


def create_app(**kwargs):
    """Create Flask Application."""
    app = Flask(__name__)

    MyUsers(app)  # my users app here =)

    app.config.update(kwargs)  # load config

    return app


def create_app_wsgi():
    """Create WSGI Application."""
    app = create_app()
    return app


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script interface for the My Users."""


@main.group("database")
def db():
    """Database operations."""


@db.command()
@with_appcontext
def createdb():
    """Create a new MyUsers database."""
    db_module.create_all()


@db.command()
@click.option("-s", "--size", default=1500)
@with_appcontext
def populatedb(size):
    """Populate the database with fake data."""
    faker = Faker()

    for _ in range(size):
        userdata = faker.simple_profile()

        user = User(
            name=userdata["name"],
            username=userdata["username"],
            email=userdata["mail"],
        )

        db_module.session.add(user)
    db_module.session.commit()
