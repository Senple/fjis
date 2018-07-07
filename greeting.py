from bottle import route, run, template, static_file, url, HTTPResponse
from bottle import get, post, request, response, error
from bottle import hook, route, response, redirect
import os
import datetime as dt

"""
サーバーコンソール上の色を変えたいけど、動いてくれない…
JUPYTER NOTEBOOK上では動くのになー
"""

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


#初期URL
@route('/')
def index():
    a = 0
    WhereIsHere(a)
    return template('index', url=url)

#Hello Worldを表示するURL
@route('/hello')
def hello():
    a = 1
    WhereIsHere(a)
    return "Hello World!"

#名前を送られたら挨拶するURL
@route('/name', method = ["GET", "POST"])
def name():
    Name = request.query.name
    now_greet = greet()
    text = now_greet + '! あなたの名前は'+ str(Name) + 'さんだね！'
    a = 2
    WhereIsHere(a)
    # print("クライアント側："+ text, "挨拶は：" + now_greet)
    return text

#404エラーの場合はリダイレクトしてページ遷移を用意
@error(404)
def oh(error):
    NASA = "i dont know! That Page is stolen by NASA"
    a = 3
    WhereIsHere(a)
    #redirect('/redirect')
    return template('redirect', url=url)


"""
今の時間に応じた挨拶を提供する
"""
def greet():
    now = dt.datetime.now()
    greet_list = ["丑三つ時です～","おはよう","こんにちは","こんばんは","夜更かしはだめですよ！"]
    time = now.hour
    if time < 3 and time >= 2:
        return greet_list[0]
    elif time <=  9 and time >5:
        return greet_list[1]
    elif time <= 17 and time > 9:
        return greet_list[2]
    elif time <=22 and time > 17:
        return greet_list[3]
    else:
        return greet_list[4]


"""
コンソール上にほかの"/URL"の情報と今いる場所を表示する
"""
def WhereIsHere(number):
    Doko_List = ["index","hello","name","redirect"]
    for i in Doko_List:
        b = "'/{url}' {url}".format(url = i)
        if i == Doko_List[number]:
            print(pycolor.UNDERLINE + b + pycolor.END)
        else:
            print(b)

#bottleを開始する魔法の言葉
run(host='localhost', port=8080, debug=True, reloader=True)
