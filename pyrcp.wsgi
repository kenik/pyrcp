#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

path = '/home/kenik/pyrcp'
if path not in sys.path:
    sys.path.append(path)
from pyrcp import app as application
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
