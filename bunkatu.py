# coding: utf-8

import sys

FILE_NAME = "logdata0803.txt"
#print "FILE NAME:" + FILE_NAME  # ファイル名出力
f = open(FILE_NAME)  # ファイルを開く
l_all_column = f.readlines()  # １行を１リストとして保管
f.close  # ファイルを閉じる

villageNumber = 0
f = open("output0.txt", "w")

for s_one_colum in l_all_column:  # 一行ずつ処理
    if(s_one_colum.find("人狼なんているわけないじゃん。みんな大げさだなあ") != -1):
        f.close
        villageNumber += 1
        if(villageNumber > 100):
            sys.exit()
        print villageNumber
        f = open("output" + str(villageNumber) + ".txt", "w")

    tmp1 = s_one_colum.replace("！", "\n")
    tmp2 = tmp1.replace("!", "\n")
    tmp3 = tmp2.replace("。", "\n")
    tmp4 = tmp3.replace("…", "\n")
    tmp5 = tmp4.replace("？", "\n")

    f.write(tmp5)
    #print s_one_colum.replace("。", "\n")
