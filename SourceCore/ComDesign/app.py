# coding=utf8
import random
import time

import pymysql
from gevent import pywsgi
from flask import Flask, request, json
from cemotn.emotion import analyze_emotion
from BaiChuan.BaiCuan import sample_sync_call
from Data.random_select import random_select
from model.check_login import is_existed, exist_user, is_null
from model.register import add_user
from model.video import get_video, random_video
from model.recording import recording
from configparser import ConfigParser

defaultencoding = 'utf-8'
app = Flask(__name__)

data = {
    "crosstalk": "一则小品",
    "joke": "一个笑话",
    "movie": "一部电影",
    "music": "一首音乐",
    "poem": "一首诗",
}

username = "root"
sum_turn = 0
positive = 0
negative = 0
flag = 0


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/score', methods=['POST'])
def score():
    global sum_turn
    global negative
    global flag
    global username
    report = None
    print(request)
    input_txt = str(json.loads(request.values.get("txt")))
    print(username)
    print(input_txt)
    label = analyze_emotion(input_txt)
    sum_turn += 1
    if flag == 1:
        if label == 1:
            report = {'type': 'video', 'video': random_video()}
        else:
            report = {'type': 'text', 'text': '还有什么我能帮到您的吗？我什么都愿意倾听。'}
        negative = 0
        flag = 0
    elif sum_turn < 2:
        report = sample_sync_call(input_txt)
    else:
        if negative < 3:
            if label == 0:
                negative += 1
            report = sample_sync_call(input_txt)
        else:
            report = sample_sync_call(input_txt)
            report['text'] = report['text'] + '\n看来您心情确实不好，我可以推荐你一段视频，可能对您有所帮助，是否愿意观看呢？'
            flag = 1
    print({'result': report})
    d = {
        'input_txt': input_txt,
        'sum_turn': sum_turn,
        'negative': negative,
        'flag': flag,
        'lable': label,
        'report': report,
        'time': time.asctime()
    }

    recording(username=username, data=d)

    print('sum_turn:', sum_turn)
    print('negative:', negative)
    print('flag:', flag)
    print('lable', label)

    return json.dumps({'result': report})


@app.route('/login', methods=['POST'])
def login():
    global username
    report = {'text': ''}
    print(request)
    username = str(json.loads(request.values.get("username")))
    password = str(json.loads(request.values.get("password")))
    print(username)
    print(password)
    if is_existed(username, password):
        report = {'text': '登录成功'}
    else:
        report = {'text': '登录失败'}
    return report


@app.route("/register", methods=['POST'])
def register():
    global username
    print('开始------------------------------')
    print(request)
    name = str(json.loads(request.values.get("name")))
    print(name)
    username = str(json.loads(request.values.get("username")))
    print(username)
    password = str(json.loads(request.values.get("password")))
    print(password)
    report = {'text': ''}
    if request.method == 'POST':
        if exist_user(username):
            report['text'] = "账号存在"
            # return redirect(url_for('user_login'))
        else:
            report['text'] = "注册成功"
            add_user(name, username, password)
    return report


@app.route("/video", methods=['GET'])
def video():
    data = get_video()
    print(data)
    dic = {
        'list': []
    }
    for i in range(len(data)):
        d = {'video_url': data[i][1], 'up': data[i][6], 'title': data[i][4], 'cover_url': data[i][5]}
        dic['list'].append(d)
    print(dic)
    return dic


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('D:\学习\pycharm_workspase\ComDesign\config.ini')
    fk = cfg.items('flask')
    app.run(host=fk[0][1], port=eval(fk[1][1]))

# -------------------------------------------------------------------------------


# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'hello world'
#
# if __name__ == '__main__':
#     app.run()
