# app.py
from back import app
from back.views import *

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
