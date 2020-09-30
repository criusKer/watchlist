# coding=utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/')   # 视图函数
def hello():
    return 'welcome!'
