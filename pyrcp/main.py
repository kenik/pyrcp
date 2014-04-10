#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import time
from pyrcp import *
import config
from pyrcp.views import *
from flask import Flask
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
from itsdangerous import URLSafeTimedSerializer

app.config.from_object('config.MyRoConfig')
app.debug = app.config["DEBUG"]
app.secret_key = "a_random_secret_key_$%#!@"
app.config["REMEMBER_COOKIE_DURATION"] = time.time() + 14 * 24 * 3600 # 14 days from now

login_serializer = URLSafeTimedSerializer(app.secret_key)
#Flask-Login Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
    login_manager.anonymous_user = Anonymous
    return User.get(userid)

@login_manager.token_loader
def load_token(token):
    max_age = app.config["REMEMBER_COOKIE_DURATION"].total_seconds()

    #Decrypt the Security Token, data = [username, hashpass]
    data = login_serializer.loads(token, max_age=max_age)

    #Find the User
    user = User.get(data[0])

    #Check Password and return user or None
    if user and data[1] == user.password:
        return user
    return None

if __name__ == '__main__':
    app.run()
