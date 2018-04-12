#!/usr/bin/env python3
#定义最上层文件路径
#该程序会修改所有的文件名字，将不是文件夹的文件按照次序排列并重新命名
import sys, os
import os.path
path = "/home/skittle/test"   #注意修改你自己的文件路径,绝对路径你懂吧
circu = 0
for index in os.listdir(path):
    print(index)
    curpath = path + '/' + index
    print(curpath)
    if os.path.isfile(curpath):      #注意到这里的isfile需要使用绝对路径进行判断
        circu += 1
        newname = str(circu)+'.'+'jpg'
        #print(newname)
        os.rename(path+'/'+index,path+'/'+newname)
