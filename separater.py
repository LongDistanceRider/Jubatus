# -*- coding: utf-8 -*-
#テキストファイルを分かち書きするプログラム
import MeCab
import sys
import re

all_node = []
limit = 0               #リミッター

m = MeCab.Tagger ("--unk-feature undefined -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

for file_number in range(1, 2):
    file_name = "village" + "1_1000" + ".txt"

    f = open(file_name)     #ファイル読み込み
    l_all_column = f.readlines()
    f.close
    for s_one_column in l_all_column:       #一行ずつ処理

        node = m.parseToNode(s_one_column)  #一行をnodeに分解
        while(node):
            all_node.append(node.surface)
            node = node.next        #次のnodeへ
            if node is None:        #すべてのnodeを調べたためブレイク
                break
        
        limit += 1
        print limit
        if limit > 10000:
            break
output_string = " ".join(all_node)
file = open ("villageRe.txt", "w")
try:
    file.write(output_string)
finally:
    file.close()