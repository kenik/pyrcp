# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
from pyrcp import *
from main import *
from views import *