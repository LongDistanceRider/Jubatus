#!/usr/bin/env python
# coding: utf-8

#Python 2 compatibility:
from __future__ import with_statement

host = '127.0.0.1'  #hostアドレス
port = 9199         #port番号
name = 'test'       #タスクを識別するZookeeperクラスタ内でユニークな名前を設定する

import sys
import random
import copy

import jubatus
from jubatus.common import Datum

####    定数定義    ####
#教師ファイル
teacher = ["teacher_comingout_50.txt", \
             "teacher_div_inq_50.txt" \
          ]
#精度比較ファイル
comparison = ["comparison.txt"]

####

#学習用データ読み込み
def loadFile(file_name):
    uni_line = []
    for line in open(file_name, 'r'):
        uni_line.append(line.decode('utf-8'))
    print "学習用データが読み込まれました" + uni_line + "[END]"
    return uni_line
        
def train(client):    
    for

    teacher_comingout = loadFile("teacher_comingout_full.txt")
    teacher_divined = loadFile("teacher_divined_full.txt")
    teacher_inquested = loadFile("teacher_inquested_full.txt")

    train_data = []
    for tech in teacher_comingout:
        train_data.append((u'comingout', Datum({u'name': tech})))

    for tech in teacher_divined:
        train_data.append((u'divined', Datum({u'name': tech})))

    for tech in teacher_inquested:
        train_data.append((u'inquested', Datum({u'name':tech})))

    random.shuffle(train_data)      #学習用データをシャッフル

    client.train(train_data)        #Jubatusにデータを渡す

def predict(client):
    comparison_comingout = loadFile("comparison_comingout.txt")
    comparison_divined = loadFile("comparison_divined.txt")
    comparison_inquested = loadFile("comparison_inquested.txt")

    data = []

    for comparison in comparison_comingout:
        data.append(Datum({u'name': comparison}))

    for comparison in comparison_divined:
        data.append(Datum({u'name': comparison}))

    for comparison in comparison_inquested:
        data.append(Datum({u'name': comparison}))

    for d in data:
        res = client.classify([d])  # 予測値リストが帰ってくる
        shogun_name = max(res[0], key=lambda x: x.score).label  # スコアが最大であるものを取得
        first_name = d.string_values[0][1]
        print shogun_name
        print first_name

if __name__ == '__main__':
    #jubatusに接続
    client = jubatus.Classifier(host, port , name)
    #学習用データを渡す
    train(client)
    #予測用データを渡し，結果を表示する
    predict(client)