# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask import Blueprint, jsonify, request
from myusers.modules.models import User

users_bp = Blueprint("users_bp", "users_bp")


@users_bp.route("/users", methods=["GET"])
def users():
    """List users (with very very simple pagionation system)."""
    # pagination parameters
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 100, type=int)

    # query
    users_records = User.query.paginate(page, size)

    # prepare the results
    results = {
        "results": [u.to_dict() for u in users_records.items],
        "pagination": {
            "count": users_records.total,
            "page": page,
            "size": size,
            "pages": users_records.pages,
        },
    }

    # hard coding way (sorry....responsability is broken)
    links = {
        "next": f"/users?page={page + 1}&size={size}",
        "previous": f"/users?page={page - 1}&size={size}",
    }

    if page == 1:
        del links["previous"]

    if page == users_records.pages:
        del links["next"]

    results["pagination"].update(links)

    return jsonify(results)


def init_module(app):
    """Factory function to initialize the models module."""

    app.register_blueprint(users_bp)
