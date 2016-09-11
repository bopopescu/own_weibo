#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8

import pymongo 
import os
import re
from pymongo import MongoClient


MONGODB_HOST = '219.224.134.222' #'localhost'
MONGODB_PORT = 27017
conn = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
MONGODB_DB = 'jln_weibo'
MONGOD_COLLECTION = 'text_num'

mongodb = conn[MONGODB_DB]
collection = mongodb[MONGOD_COLLECTION]
results = collection.find()

#conn = pymongo.MongoClient()
#collc = conn.jln_weibo.content
#a = collc.find_one({"comment_count":385})
os.chdir(r'/home/jiangln/own_weibo/raw_data/content/number')
files_name = []
for files in os.listdir(r'/home/jiangln/own_weibo/raw_data/content/number'):
    files_name.append(files)

#a = '(\d\d:){2}(\d\d)\s(.*)\d'
#pattern = re.compile(a)

#contents = []
for files in files_name:
    f = open(files,'r')
    for line in f:
        num = {}
        t = line.replace('\N','0').strip('\n').split('\t')
        #print t
        num['mid'] = t[0]
        num['read_num'] = t[1]
        num['com_num'] = t[2]
        num['repo_num'] = t[3]
        num['like_num'] = t[4] 
        collection.insert(num)
        #contents.append(line)
        #result = pattern.findall(line)
        #print result[0][2]

 
