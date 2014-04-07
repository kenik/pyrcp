# -* coding: utf-8 -*-
from hashlib import md5
from pyrcp import *
import pyrcp.db as pydb
from flask import Flask, request, redirect, render_template
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
from itsdangerous import URLSafeTimedSerializer

login_serializer = URLSafeTimedSerializer(app.secret_key)

class User(UserMixin):
    def __init__(self, userid, user_pass, account_id):
        self.id = userid
        self.user_pass = user_pass
        self.account_id = account_id

    def get_auth_token(self):
        """
        Encode a secure token for cookie
        """
        data = [str(self.id), self.user_pass]
        return login_serializer.dumps(data)

    @staticmethod
    def get(userid):
        """
        Static method to search the database and see if userid exists.  If it
        does exist then return a User Object.  If not then return None as
        required by Flask-Login.
        """
        #For this example the USERS database is a list consisting of
        #(user,hased_password) of users.
        db = pydb.get_db()
        cursor = db.cursor()
        sql = "SELECT `userid`, `user_pass`, `account_id` FROM `login` WHERE `userid`='%s'"
        cur = cursor.execute(sql % (userid))
        users = cursor.fetchall()
        for user in users:
            if user[0] == userid:
                return User(user[0], user[1], user[2])
        return None

    def get_acc_id(self):
        return self.account_id

    def get_id(self):
        return self.id
def hash_pass(password):
    return md5(password).hexdigest()

def main():
    pass

if __name__ == '__main__':
    main()
