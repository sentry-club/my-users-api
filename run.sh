# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

export $(cat .env | xargs)

docker-compose up -d
