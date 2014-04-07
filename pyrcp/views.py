# -*- coding: utf-8 -*-
from pyrcp import app
from pyrcp.funcs import *
from pyrcp.user import *
from flask import Flask, request, redirect, render_template, flash, url_for
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
from itsdangerous import URLSafeTimedSerializer

@app.before_request
def load_user_i():
    if current_user.get_id():
        user = True
    else:
        user = False
    app.logged_in = user

# Шаблоны и страницы
@app.route('/')
def show_main():
    if current_user.get_id():
        user = current_user
    else:
        user = None
    userser = current_user
    return render_template('show_main.html', app=app, user=user)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user:
        redirect("/")
    error = None
    if request.method == "POST":
        user = User.get(request.form['userid'])
        if not user:
            error = 'Invalid username'
            return render_template('login.html', app=app, error=error)
        if user and hash_pass(request.form['user_pass']) == user.user_pass:
            login_user(user, remember=False)
            return redirect(request.args.get("next") or "/")
        else:
            error = 'Invalid password'
            return render_template('login.html', app=app, error=error)
    return render_template('login.html', app=app, error=error)

@app.route('/my_acc', methods=['GET', 'POST'])
@login_required
def my_acc():
    error = None
    if current_user.get_id():
        userid = current_user.get_acc_id()
    db = pydb.get_db()
    cursor = db.cursor()
    sql = "SELECT `name`, `class`, `guild_id`, `base_level`, `job_level`, `base_exp`, `job_exp` from `char` where `account_id`='%s' "
    cur = cursor.execute(sql % (userid))
    if cur == 0:
        chars = None
        error = "You have no characters yet"
        return render_template('my_acc.html', error=error, app=app, chars=chars)
    chars = cursor.fetchall()
    sql = "SELECT `account_id`, `userid`, `sex`, `email`, `group_id`, `state`, `logincount`, `birthdate`, `lastlogin`, `last_ip` from `login` where `account_id`=%s "
    cur = cursor.execute(sql % (current_user.get_acc_id()))
    #user = get_acc_info(userid)
    user = cursor.fetchone()
    app.jinja_env.globals.update(get_class_name=get_class_name)
    return render_template('my_acc.html', error=error, app=app, chars=chars, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user:
        redirect("/")
    error = None
    if request.method == "POST":
        user = User.get(request.form['userid'])
        if not user:
            error = 'Invalid username'
            return render_template('login.html', app=app, error=error)
        if user and hash_pass(request.form['user_pass']) == user.user_pass:
            login_user(user)
            return redirect(request.args.get("next") or "/")
        else:
            error = 'Invalid password'
            return render_template('login.html', app=app, error=error)
    return render_template('login.html', app=app, error=error)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_main'))

'''
    Rankings
'''
@app.route('/ranking')
@app.route('/ranking/guild')
def ranking_guild():
    guilds = get_guilds_ranks()
    app.jinja_env.globals.update(get_guild_members_count=get_guild_members_count)
    return render_template('rank_guild.html', app=app, guilds=guilds)

@app.route('/ranking/char')
def ranking_char():
    chars = get_chars_ranks(0,20)
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_char.html', app=app, chars=chars)

@app.route('/ranking/zeny')
def ranking_zeny():
    chars = get_chars_ranks(0,20, '`zeny`')
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_zeny.html', app=app, chars=chars)

@app.route('/ranking/pvp_death')
def ranking_pvp_death():
    chars = get_chars_ranks(0,20, '`pvp_death`')
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_pvp_death.html', app=app, chars=chars)

@app.route('/ranking/pvp_kills')
def ranking_pvp_kills():
    chars = get_chars_ranks(0,20, '`pvp_kills`')
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_pvp_kills.html', app=app, chars=chars)

@app.route('/ranking/woe_death')
def ranking_woe_death():
    chars = get_chars_ranks(0,20, '`woe_death`')
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_woe_death.html', app=app, chars=chars)

@app.route('/ranking/woe_kills')
def ranking_woe_kills():
    chars = get_chars_ranks(0,20, '`woe_kills`')
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('rank_woe_kills.html', app=app, chars=chars)

@app.route('/guild/<int:guild_id>')
def show_guild(guild_id):
    guild = get_guild_info(guild_id)
    chars = get_guild_members(guild_id)
    app.jinja_env.globals.update(get_guild_members_count=get_guild_members_count)
    app.jinja_env.globals.update(get_class_name=get_class_name)
    return render_template('info_guild.html', app=app, guild=guild, chars=chars)

@app.route('/char/<int:char_id>')
def show_char(char_id):
    char = get_char_info(char_id)
    app.jinja_env.globals.update(get_class_name=get_class_name)
    app.jinja_env.globals.update(get_party_name=get_party_name)
    app.jinja_env.globals.update(get_guild_name=get_guild_name)
    return render_template('info_char.html', app=app, char=char)

