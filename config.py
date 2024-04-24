#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6634064190:AAH8iv5BXtIp_c4ucv3kgcR3MpN25GdSaXA")
    API_ID = int(os.environ.get("API_ID", "26181533"))
    API_HASH = os.environ.get("API_HASH", "961f8a38f9d9d079100ba56fcbb9ea9b7")
    AUTH_USERS = "6329158981"


