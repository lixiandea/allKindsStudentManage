#!/usr/bin/env python3
stuInfos = []
def menu():
    print("""×××××××学生管理系统××××××××××××
            1、添加学生信息  
            2、删除学生信息
            3、修改学生信息
            4、查询学生信息
            5、显示所有学生信息
            6、退出系统  """)
    return True

def printInfo():
    for index in range(0,len(stuInfos)):
        print("姓名：{}，性别：{}，手机号码：{} ".format(
            stuInfos[index]["name"],stuInfos[index]["sex"],stuInfos[index]["phone"])
            )

def insInfo():
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    phone = input("请输入联系电话：")
    stuInfo = {}
    stuInfo.__setitem__("name", name)
    stuInfo.__setitem__("sex", sex)
    stuInfo.__setitem__("phone", name)
    stuInfos.append(stuInfo)

def delStu():
    name = input("请输入删除学生姓名：")
    for index in range(0,len(stuInfos)):
        #print(stuInfos[index]["name"])      
        if stuInfos[index]["name"] == name:
            del stuInfos[index]
            return 1
    print("未找到名字，删除失败！")
    return 0

def changeInfo():
    name = input("请输入要修改的学生的名字： ")
    key = int(input("""
    请输入要修改的数据项：
    1、性别
    2、电话"""))
    new = input("请输入新的信息： ")
    for index in range(0,len(stuInfos)):
            #print(stuInfos[index]["name"])      
        if stuInfos[index]["name"] == name:
            if key == 1:
                stuInfos[index]["sex"] = new
            if key == 2:
                stuInfos[index]["max"] = new
def searchInfo():
    key = int(input("""请输入您要查找的选项：
                        1、名字
                        2、性别
                        3、电话号码
                        """))
    new = input("请输入查找依据： ")
    for index in range(0,len(stuInfos)):
        for index in range(0,len(stuInfos)):
            if key == 1:
                if stuInfos[index]["name"] == new:
                    print("姓名：{}，性别：{}，手机号码：{} ".format(
                    stuInfos[index]["name"],stuInfos[index]["sex"],stuInfos[index]["phone"])
                    )
            if key == 2:
                if stuInfos[index]["sex"] == new:
                    print("姓名：{}，性别：{}，手机号码：{} ".format(
                    stuInfos[index]["name"],stuInfos[index]["sex"],stuInfos[index]["phone"])
                    )
            if key == 3:
                if stuInfos[index]["phone"] == new:
                    print("姓名：{}，性别：{}，手机号码：{} ".format(
                    stuInfos[index]["name"],stuInfos[index]["sex"],stuInfos[index]["phone"])
                    )
    
def loadfile():
    file = open("/home/skittle/Code/allrecord.dat")
    line = file.readline()
    while line:
        test = line.split()
        stuInfo = {}
        stuInfo["name"] = test[0]
        stuInfo["sex"] = test[1]
        stuInfo["phone"] = test[2]
        stuInfos.append(stuInfo)
        line = file.readline()
    file.close()

def savefile():
    file = open("/home/skittle/Code/allrecord.dat", 'w')
    for index in range(0, len(stuInfos)):
        file.write("%s %s %s\n"%(stuInfos[index]["name"],
        stuInfos[index]["sex"],stuInfos[index]["phone"]))
    file.close()
    

loadfile()
while (menu()):
    key = int(input("请选择功能： "))    
    if key == 1:
        insInfo()
        savefile()
    if key == 2:
        delStu()
        savefile()
    if key == 3:
        changeInfo()
        savefile()
    if key == 4:
        searchInfo()
    if key == 5:
        printInfo()
    if key == 6:
        savefile()        
        print("学生管理系统为您服务！再见。")
        exit()
