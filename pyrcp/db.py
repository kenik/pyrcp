# -*- coding: utf-8 -*-
from flask import Flask, g
import MySQLdb
from pyrcp import app

def connect_db():
    """Подключение к базе данных."""
    db = MySQLdb.connect(host=app.config['HOST'], user=app.config['USERNAME'], passwd=app.config['PASSWORD'], db=app.config['DATABASE'], charset=app.config['CHARSET'])
    return db

def get_db():
    """Открываем соединение, если оно еще не было открыто."""
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = connect_db()
    return g.mysql_db

def get_cursor():
    """Открываем соединение, если оно еще не было открыто."""
    db = get_db()
    return db.cursor()

@app.teardown_appcontext
def close_db(error):
    """После запроса следует закрыть соединение."""
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
