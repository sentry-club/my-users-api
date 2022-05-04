# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from importlib import import_module


MODULES = [
    "myusers.modules.models",
    "myusers.modules.users",
]


def init_modules(app):
    """Factory app function."""

    for module in MODULES:
        mod = import_module(module)
        mod.init_module(app)
