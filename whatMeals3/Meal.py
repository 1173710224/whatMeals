# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:31:37 2019

@author: C-82
"""


import numpy as np
import time
import json
'''
List是要进行查找的所有文件名的一个数组
'''
def Find(List):
    expectation = 0
    tmpstring = ''
    OBJ = Meal
    for string in List:
        obj = Meal(string)
        tmpexpectation = obj.Expectation()
        if tmpexpectation > expectation:
            expectation = tmpexpectation
            tmpstring = string
            OBJ = obj
    OBJ.left_eaten_num = OBJ.left_eaten_num - 1
    OBJ.Check()
    OBJ.last_eaten_time = time.time()
    OBJ.ChanData()
    tmpstring = tmpstring.replace("\n","")
    name_place = tmpstring.split("_")
    return name_place

def Reset():
    IO_breakfast = open("1早饭.txt","r")
    IO_lunch = open("2午饭.txt","r")
    IO_dinner= open("3晚饭.txt","r")
    IO_night = open("4夜宵.txt","r")
    list_breakfast = IO_breakfast.readlines()
    list_lunch = IO_lunch.readlines()
    list_dinner = IO_dinner.readlines()
    list_night = IO_night.readlines()
    for string in list_breakfast:
        a = Meal(string)
        a.ChanData()
    for string in list_lunch:
        a = Meal(string)
        a.ChanData()
    for string in list_dinner:
        a = Meal(string)
        a.ChanData()
    for string in list_night:
        a = Meal(string)
        a.ChanData()
    IO_breakfast.close()
    IO_lunch.close()
    IO_dinner.close()
    IO_night.close()

class Meal:
    def __init__(self,name_place):
        List = name_place.split("_")
        self.last_eaten_time = 0.0
        self.left_eaten_num = 5
        self.name = List[0]
        self.place = List[1]
        self.name_place = name_place
        #self.GetData()
    #这个函数用来返回吃当前这个范德概率
    def Expectation(self):
        if (time.time() - self.last_eaten_time) < 24 * 3600 * 5:
            return 0
        return np.random.uniform(0,float(self.left_eaten_num))
    def Check(self):
        if self.left_eaten_num == 0:
            self.left_eaten_num = 5
    def CreFile(self):
        self.name_place = self.name_place.replace('\n','')
        full_path = 'data' + '//' + self.name_place + '.json'
        file = open(full_path,'r+')
        file.write('1')
        file.close()
    #更新文件内容
    def ChanData(self):
        self.name_place = self.name_place.replace('\n','')
        full_path = 'data' + '//' + self.name_place + '.json'
        file = open(full_path,'w')
        file.truncate()
        write_dict ={"name":self.name,"place":self.place,"time":self.last_eaten_time,"num":self.left_eaten_num}
        file.write(str(write_dict))
        file.close()
    #从文件中加载数据
    def GetData(self):
        self.name_place = self.name_place.replace('\n','')
        full_path = 'data' + '//' + self.name_place + '.json'
        file = open(full_path,'r+')
        string = json.load(file)
        string = json.loads(string)
        self.name = string["name"]
        self.place = string["place"]
        self.last_eaten_time = string["time"]
        self.left_eaten_num = string["num"]
        file.close()

