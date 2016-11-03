# -*- coding: utf-8 -*-
import numpy as np
#import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt  
from pymongo import MongoClient
import redis
import networkx as nx
import logging
import time
import community
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',filename='log/text.log',filemode='a')
logger = logging.getLogger(__name__)
logger.info('Start....')
hdlr = logging.FileHandler('log/text.log.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)

#import numpy as np
#from  IPython.core.utils.terminal import get_terminal_size

MONGODB_HOST = '219.224.134.222' #'localhost'
MONGODB_PORT = 27017
conn = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
MONGODB_DB = 'jln_weibo'
MONGOD_COLLECTION = 'allinfo'

db = conn[MONGODB_DB]
collection = db[MONGOD_COLLECTION]
results = collection.find()

r = redis.StrictRedis(host='219.224.134.222', port=6379, db=1)
#r.set('foo','bar')
#print r.get('foo')

def allinfo(): #好友数/关注数的比例
    a = collection.find()
    ratio = []
    #j = 0
    for i in a:
        uid = i['id']
        try:
            ra = float(i['friends_num'])/float(i['atten_num'])
        except ZeroDivisionError:
            ra = 0
        ratio.append(ra)
        #print uid,ra
        r.hset('ratio',uid,ra)

def find_text(MONGOD_COLLECTION,uid):
	collection = db[MONGOD_COLLECTION]
	a = collection.find({'uid':uid}).limit(200)
	return a


def info_count():
	a = collection.find()
	uid = []
	friends_num = []
	atten_num = []
	fans_num = []
	# j = 0
	for i in a:
		# j += 1
		uid.append(i['id'])
		friends_num.append(i['friends_num'])
		atten_num.append(i['atten_num'])
		fans_num.append(i['fans_num'])
		# if j>6:
		# 	break
	f1 = open('/home/jiangln/own_weibo/raw_data/for_cluster.txt','w')
	f2  = open('/home/jiangln/own_weibo/raw_data/cluster_uid.txt','w')
	lines = []
	for i in range(0,len(uid)):
		line = ' '.join(['1',friends_num[i],'2',atten_num[i],'3',fans_num[i]])+'\n'
		lines.append(line)
		f2.write(uid[i]+'\n')
	f1.write('%s %s %s\n' % (len(uid),3,int(len(uid))*3))  #行数，列数，特征值总数
	f1.writelines(lines)


def plot_ratio():
    ratio = r.hvals('ratio')
    sort = []
    for i in ratio:
    	sort.append(float(i))
    sort = sorted(sort)
    x = range(0,len(sort))
    print len(x),len(sort),sort[0:5]
    plt.scatter(x,sort)
    plt.savefig('ratio.png', dpi=75)

def relation(): #节点度
	collection = db['f_relation_wan']
	a = collection.find()
	in_degree = {} #入度
	out_degree = {} #出度
	for i in a:
		if i['followed'] in in_degree:
			in_degree[i['followed']] += 1
			#print '1!!!!' + i['followed'],in_degree[i['followed']]
		else:
			in_degree[i['followed']] = 1
			#print '2!!!!' + i['followed'],in_degree[i['followed']]

		if i['follower'] in out_degree:
			out_degree[i['follower']] += 1
			#print '3!!!!' + i['follower'],out_degree[i['follower']]
		else:
			out_degree[i['follower']] = 1
			#print '4!!!!' + i['follower'],out_degree[i['follower']]
	#print out_degree['3994142429']
	for k ,v in in_degree.items():
		r.zadd('f_wan_in_degree',v,k)
	for k,v in out_degree.items():
		r.zadd('f_wan_out_degree',v,k)		
	plot_du('f_wan_in_degree','wan_in_degree0.png')	
	plot_du('f_wan_out_degree','wan_out_degree0.png')	

def plot_du(redis_name,img_name):
	a = r.zrange(redis_name,0,-1, withscores=True)
	degree = []
	for i in a:
		degree.append(i[1]) #节点度的大小
	#s = pd.Series(np.log(degree))
	s = pd.Series(degree)
	prob = s.value_counts()/s.count()
	#散点图    纵坐标  节点度为k的概率；横坐标  节点度的大小
	#plt.plot(x,degree,color='r')
	#f1 = plt.figure(1)
	#print prob.index,prob.values
	plt.scatter(prob.index,prob.values,color ='blue')
	ax = plt.gca()
	l = [min(prob.index),max(prob.index),min(prob.values),max(prob.values)]
	ax.axis(l)  #l是刻度范围，x最小，x最大，y最小，y最大
	#plt.loglog(x,y)
	ax.set_xscale('log')#'log'指对坐标轴刻度取对数，按对数取，不是转为对数
	ax.set_yscale('log')
	
	plt.show()
	plt.savefig(img_name, dpi=75)	

def both_degree(logger):
	both = r.zrange('f_both_in_degree',0,-100000)  #把同时有出入度的点取出来，然后读他们之前的关系组成邻接矩阵
	collection = db['relation']
	#print both
	logging.info('%s',both)

	#a = collection.find(timeout=False)
	a = collection.find({'follower':{'$in':both},'followed':{'$in':both}})
	logging.info(a.count())
	print a.count()
	for i in a:
		print i
		#if i['follower'] in both and i['followed'] in both:
		db['relation0'].insert(i)



def filter_both_degree():
	collection = db['filter_both_in']
	r = redis.StrictRedis(host='219.224.134.222', port=6379, db=2)
	#a = collection.find(timeout=False)
	#for i in a:
	#	r.sadd(i['followed'],i['follower'])   #set里的键是被关注的人，值是关注它的人
	names = r.keys('*')
	for name in names :
		for follower in r.smembers(name):
			rel = {}
			rel['follower'] = follower
			rel['followed'] = name
			collection.insert(rel)


def graph():
	collection1 = db['f_relation_wan']
	#collection2 = db['filter_both_in']
	#new_collction = db['f_relation_wan']
	a = collection1.find()
	#f = collection2.find()
	G1 = nx.DiGraph()
	for i in a:
		#print i
		G1.add_edge(i['follower'],i['followed'])
	#G2 = nx.DiGraph()
	#for i in f:
	#	G2.add_edge(i['follower'],i['followed'])
	G1 = G1.to_undirected()
	print G1.size(),G1.number_of_nodes()
	draw_partition(G1)
	kclique(G1)

def kclique(g):
	for k in xrange(2,3):
		print '**********k值：%d*************' % k
		start_time = time.clock()
		rst_com = find_community(g,k)
		end_time = time.clock()
		print '计算耗时（秒）：%.3f' % (end_time-start_time)
		print '生成社区数：%d' % len(rst_com)
		print rst_com
	#G2un = G2.to_undirected()
	#print nx.average_clustering(G1)
	#print nx.transitivity(G1)
	#print nx.average_clustering(G2un)
	#print nx.transitivity(G2un)
	#nx.draw(G)
	#plt.savefig('draw.png')
	#print nx.average_clustering(G)
	#degree = list(G.out_degree(G.nodes()).values())
	#x = range(len(degree))
	#y = [float(z)/float(sum(degree)) for z in degree]
	# edge = G1.edges()
	# both = set(r.zrange('f_both_in_degree',-10000,-1))
	# for i in edge:
	# 	print i 
	# 	if i[0] in both and i[1] in both:
	# 		print 'yes!!!!!!!!!!!!!!!!'
	# 		print i[0],[1]
	# 		rel = {}
	# 		rel['follower'] = i[0]
	# 		rel['followed'] = i[1]
	# 		new_collction.insert(rel)
	#plt.loglog(x,y)
	#plt.savefig('try.png')

def find_community(graph,k):
	return list(nx.k_clique_communities(graph,k))

def draw_partition(G1):
	partition = community.best_partition(G1)
	size = float(len(set(partition.values())))
	pos = nx.spring_layout(G1)
	count = 0.

	for com in set(partition.values()) :
	    count = count + 1.
	    list_nodes = [nodes for nodes in partition.keys()
	                                if partition[nodes] == com]                 
	    nx.draw_networkx_nodes(G1, pos, list_nodes, node_size = 50,
	                                node_color = str(count / size))

	nx.draw_networkx_edges(G1,pos,with_labels = True, alpha=0.5 )
	plt.show()
	plt.savefig('partition.png')

if __name__ == '__main__':
    #allinfo()
    #relation()
    #plot_du()
    #both_degree(logger)
    graph()
    #plot_ratio()
	#info_count()
	#filter_both_degree()
