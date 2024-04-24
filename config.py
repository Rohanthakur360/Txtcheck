#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7061439554:AAHDXBBktV5P4O6sjBLamdX2hhvBN7uPSl0")
    API_ID = int(os.environ.get("API_ID", "20963688"))
    API_HASH = os.environ.get("API_HASH", "964a26dc404aa5e12dfe82ea94ae7ae3")
    AUTH_USERS = "6867189163"


