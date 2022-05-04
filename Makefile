# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Sentry Club.
#
# My Users is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

setup_release: create_release associate_commits

create_release:
	sentry-cli --url $(MY_USERS_SENTRY_DSN) releases -o $(SENTRY_ORG) new -p $(MY_USERS_SENTRY_APP) $(MY_USERS_SENTRY_TAG_ENVIRONMENT)

associate_commits:
	sentry-cli --url $(MY_USERS_SENTRY_DSN) releases -o $(SENTRY_ORG) -p $(MY_USERS_SENTRY_APP) set-commits --auto $(MY_USERS_SENTRY_TAG_ENVIRONMENT)
