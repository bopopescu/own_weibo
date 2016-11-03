# -*- coding: utf-8 -*-
from pymongo import MongoClient
import redis 
import time
import numpy as np
# import matplotlib
# matplotlib.use('Agg') 
#import matplotlib.pyplot as plt  
from cluster_jln import try_kmeans,try_AP
from sklearn import preprocessing
from scipy import sparse  #稀疏矩阵



MONGODB_HOST = '219.224.134.222' #'localhost'
MONGODB_PORT = 27017
conn = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
MONGODB_DB = 'jln_weibo'
MONGOD_COLLECTION = 'f_relation_wan'


r = redis.StrictRedis(host='219.224.134.222', port=6379, db=1)

db = conn[MONGODB_DB]
collection = db[MONGOD_COLLECTION]

def trans():
	t0 = time.time()
	mongo = collection.find()
	for uids in mongo:
		follower = uids['follower']
		followed = uids['followed']
		r.sadd('fans_of_'+followed,follower)
		r.sadd('focus_by_'+follower,followed)
	t = time.time()-t0
	print t

def redis2dict():
	time0 = time.time()
	length = r.zcard('f_wan_in_degree')
	redis_uid = r.zrange('f_wan_in_degree',0,length)
	uid_list = []
	for i in redis_uid:
		uid_list.append(i)
	write = []
	dist = np.zeros([length,length])
	f = open('redis_dist.txt','a')
	c = 0
	total = 0
	for i in xrange(0,length):
		followed_by_i,follower_of_i = follow_set(uid_list[i])
		relation = followed_by_i.union(follower_of_i)
		print i 
		for uid in relation:
			try:
				j=uid_list.index(uid)
			except:
				continue
			followed_by_j,follower_of_j = follow_set(uid)
			relation_j = followed_by_j.union(follower_of_j)
			try:
				co_fans = len(follower_of_j.intersection(follower_of_i))/float(len(follower_of_j.union(follower_of_i)))  #杰卡德相似性，交集比并集
			except:
				co_fans = 0
			try:
				co_focus = len(followed_by_j.intersection(followed_by_i))/float(len(followed_by_j.union(followed_by_i)))
			except:
				co_focus = 0

			friend = 1
			if uid_list[i] in relation_j :
				friend += 1

			#print uid_list[i],uid,co_fans,co_focus,friend
			dist[i][j] = 0.2*co_fans+0.01*friend+0.6*co_focus
			#dist[i][j] = co_user + 0.1*friend
			dist[j][i] = dist[i][j]
			#print dist[i][j]
			total += dist[i][j]	
			c += 1		
			line = str(i)+' '+str(j)+' '+str(uid_list[i])+' '+str(uid_list[j])+' '+str(co_fans)+' '+str(co_focus)+' '+str(friend)+' '+str(dist[i][j])+'\n'
			#line = str(i)+' '+str(j)+' '+str(uid_list[i])+' '+str(uid)+' '+str(co_user)+' '+str(friend)+' '+str(dist[i][j])+'\n'
			#write.append[line]
			f.write(line)

	total = total/c
	for i in xrange(0,length):
		dist[i][i]=total
	#print dist,type(dist)
	time1 = time.time()-time0
	print time1
	kmeans = try_kmeans(dist)
	AP = try_AP(dist,total)


def follow_set(uid):
	followed_by_i = r.smembers('focus_by_'+uid)
	follower_of_i = r.smembers('fans_of_'+uid)
	return followed_by_i,follower_of_i 


def use_dist(n_clusters = 5):
	time0=time.time()
	f = open('redis_dist.txt','r')
	content = f.readlines()
	length = 9997
	dist = np.zeros([length,length])
	for line in content:
		a = line.strip('\n').split(' ')
		dist[int(a[0])][int(a[1])] = 1#float(a[4])+float(a[5])+float(a[6])*0.001
	#对角线
	#preference = new_dist[0][0]
	dist_nor = preprocessing.normalize(dist,norm='l1')
	time1 = time.time()-time0
	print 'time spend:'+ str(time1)

	labels = try_kmeans(dist_nor,n_clusters)
	#AP = try_AP(new_dist,total)	
	return labels

def plot(dist_nor):
	plt.imshow(dist_nor, interpolation='nearest')  
	plt.xlabel('user')  
	plt.ylabel('user')  
	plt.xticks(range(length))  
	plt.yticks(range(length))  
	plt.show()  
	plt.savefig('0904_dots.png',dpi=75)

def test():
	data = np.array([[1,2,3],[2,3,4],[5,6,7]])
	x_p = data[:, :2] # 取前2列  
	y_p = data[:,  2] # 取第3列  
	x = (sparse.csc_matrix((y_p, x_p.T)).astype(float))[:, :].todense()  
	nUser = x.shape[0] #0是行数  1是列数
	#print type(x),type(x[0]) 
	print x

def read_dist(): #并没有use_dist()建个空矩阵再存值的快
	time0=time.time()
	data = np.loadtxt('redis_dist.txt')  
	x_p = data[:, :2] # 起、止uid
	y_p = data[:,  4]+data[:,5]+data[:,6]*0.001 # 距离
	x = (sparse.csc_matrix((y_p, x_p.T)).astype(float))[:, :].todense()  #用户和值的矩阵
	nUser = x.shape[0] 
	time1 = time.time()-time0
	print 'time spend:'+ str(time1)
	print x.shape
	print x[9996,2601]
	n_clusters = 5
	#kmeans = try_kmeans(x,n_clusters)
	return x

#input:邻接矩阵、每类的点的索引
def cal_modularity(m,clusters):
	#print type(clusters),len(clusters)
	#print 'clusters:',clusters
	Q = 0
	m = np.array(m)
	degree = np.sum(m,axis=0)
	cal = 0
	total_degree = float(m.sum())
	#print clusters
	for node_list in clusters:#0,2
		#print len(node_list),type(node_list)
		tot = 0
		in_degree = 0
		for i in range(len(node_list)):#0
			for j in range(len(node_list)):#2
				if i == j:
					continue
				in_degree += m[node_list[i]][node_list[j]]
			tot += degree[node_list[i]]    
		Q += in_degree/total_degree - (tot/total_degree)**2
	#print Q
	return Q



def e_modularity(G, C):
    """ 
    Calculates the global modularity by summing over each community. 
    Should be deprecated.
    Args:
    G: Graph named tuple
    C: Community structure
    Returns:
    q: Modularity of the network with the provided community structure
    """
    A, m, n, k = G
    q = 0.0
    for com, c in C:
        rowslice = A[c,:]
        data = rowslice.data
        indices = rowslice.indices
        q += ((1.0/(2*m))*np.sum(data[np.in1d(indices, c)]) -
             (C.strength[com]/(2*m))**2)
    print q
    return q


'''另一个函数 np.in1d ，测试一个数组的值和另一个的关系，返回一个布尔数组：

In [181]: values = np.array([6, 0, 0, 3, 2, 5, 6])
In [182]: np.in1d(values, [2, 3, 6])
Out[182]: array([ True, False, False, True, True, False, True], dtype=bool)'''

if __name__ == '__main__':
	#a = use_dist()
	m = [[0,1,2,3,4],[0,0,4,5,6],[0,0,0,7,8],[0,0,0,0,9],[0,0,0,0,0]]
	clusters = [[0,2],[1,4,3]]
	cal_modularity(m,clusters)