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
MONGOD_COLLECTION = 'relation'

db = conn[MONGODB_DB]
collection = db[MONGOD_COLLECTION]
results = collection.find()

#conn = pymongo.MongoClient()
#collc = conn.jln_weibo.content
#a = collc.find_one({"comment_count":385})
os.chdir(r'/home/jiangln/own_weibo/raw_data/fans_focus')
files_name = []
for files in os.listdir(r'/home/jiangln/own_weibo/raw_data/fans_focus'):
    files_name.append(files)

def allinfo():
    a = '(\d\d:){2}(\d\d)\s(.*)\s\d'
    pattern = re.compile(a)
    contents = []
    for files in files_name:
        f = open(files,'r')
        i = 0
        for line in f:
            contents.append(line)
            #result = pattern.findall(line)
            #print result
            #print result[0][2]
            t = line.split('\t')
            info = {}
            info['id'] = t[0]
            info['uname'] = t[1]
            info['location'] = t[2]
            info['sex'] = t[3]
            info['birth'] = t[4]
            info['reg_time'] =t[5]
            info['des'] = t[6]
            info['fans_num'] = t[7]
            info['atten_num'] = t[8]
            info['friends_num'] = t[9]
            info['tag'] = t[10]
            collection.insert(info)
        
def fans():
    for files in files_name:
        f = open(files,'r')
        for line in f:
            t = line.split('\n')[0].split('\t')
            #print t
            rel = {}
            rel['followed'] = t[0]
            rel['follower'] = t[1]
            collection.insert(rel)

if __name__ == '__main__':
    fans()
