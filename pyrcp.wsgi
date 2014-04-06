#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, logging
logging.basicConfig(stream=sys.stderr)

path = '/home/sites/py.korefan.info/pyrcp'
if path not in sys.path:
    sys.path.append(path)
from pyrcp import app as application
if __name__ == '__main__':
    application.run(debug=True)
