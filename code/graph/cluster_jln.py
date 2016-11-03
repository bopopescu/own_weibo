# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 22:26:46 2016

@author: NaNa
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn.cluster import KMeans

from sklearn.cluster import AffinityPropagation
from sklearn import metrics

from pymongo import MongoClient
import redis 
import time

MONGODB_HOST = '219.224.134.222' #'localhost'
MONGODB_PORT = 27017
conn = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
MONGODB_DB = 'jln_weibo'
MONGOD_COLLECTION = 'f_relation_wan'


r = redis.StrictRedis(host='219.224.134.222', port=6379, db=1)

db = conn[MONGODB_DB]
collection = db[MONGOD_COLLECTION]
#results = collection.find()
def dist():
	time0 = time.time()
	length = r.zcard('f_wan_in_degree')
	#length = 10
	uid_list = r.zrange('f_wan_in_degree',0,length)
	write = []
	dist = np.zeros([length,length])
	f = open('dist.txt','a')
	c = 0
	total = 0
	#for i in xrange(0,length-1):
	for i in xrange(5,length-1):
		followed_by_i,follower_of_i = follow_set(uid_list[i])
		#for j in xrange(i+1,length):
		if i==5:   #交集  并集 都只有那些元素  可以从这些元素里找
			start_len = 2305
		else:
			start_len = i+1
		for j in xrange(start_len,length):
			print i,j
			c += 1
			followed_by_j,follower_of_j = follow_set(uid_list[j])
			try:
				co_fans = len(follower_of_j.intersection(follower_of_i))/float(len(follower_of_j.union(follower_of_i)))  #杰卡德相似性，交集比并集
			except:
				co_fans = 0
			try:
				co_focus = len(followed_by_j.intersection(followed_by_i))/float(len(followed_by_j.union(followed_by_i)))
			except:
				co_focus = 0
			friend = is_friend(uid_list[i],uid_list[j])
			#print co_fans,co_focus,friend
			dist[i][j] = 0.2*co_fans+0.2*friend+0.6*co_focus
			dist[j][i] = dist[i][j]
			total += dist[i][j]
			line = str(i)+' '+str(j)+' '+str(uid_list[i])+' '+str(uid_list[j])+' '+str(co_fans)+' '+str(co_focus)+' '+str(friend)+' '+str(dist[i][j])+'\n'
			#write.append[line]
			f.write(line)

	total = total/c
	for i in xrange(0,length):
		dist[i][i]=total
	#print dist,type(dist)
	time1 = time.time()-time0
	print time1
	kmeans = try_kmeans(dist)
	print '================================'
	AP = try_AP(dist,total)

	#从redis把10000个人取出来  还有他们的关系   然后按人取粉丝 关注

def write_uid(uid_list):
	f = open('uid_list.txt','w')
	for i in uid_list:
		f.write(i+'\n')
	f.close()

def is_friend(a,b):
	ii = collection.find_one({'follower':a,'followed':b})
	jj = collection.find_one({'follower':b,'followed':a})
	if ii and jj:
		return 1
	else:
		return 0


def follow_set(uid):
	followeds = collection.find({'follower':uid})
	followed_by_i = set()
	followed_by_i.add(k['followed'] for k in followeds)
	# followed_by_i = []
	# for k in followeds:
	# 	followed_by_i.append(k['followed'])
	# followed_by_i = set(followed_by_i)

	followers = collection.find({'followed':uid})
	follower_of_i = set()
	follower_of_i.add(k['follower'] for k in followers)
	# follower_of_i = []
	# for k in followers:
	# 	follower_of_i.append(k['follower'])
	# follower_of_i = set(follower_of_i)
	return followed_by_i,follower_of_i


def try_kmeans(X,n_clusters):
	t0 = time.time()
	k_means = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
	k_means.fit(X)
	t_batch = time.time() - t0
	print 'kmeans spend:',t_batch
	k_means_labels = k_means.labels_
	k_means_cluster_centers = k_means.cluster_centers_
	k_means_labels_unique = np.unique(k_means_labels)

	print 'k_means_labels',k_means_labels
	print 'k_means_cluster_centers',k_means_cluster_centers
	print 'k_means_labels_unique',k_means_labels_unique


	# colors = ['#4EACC5', '#FF9C34', '#4E9A06']
	# n_clusters = 3
	# ax = plt.gca()
	# for k, col in zip(range(n_clusters), colors):
	#     my_members = k_means_labels == k
	#     cluster_center = k_means_cluster_centers[k]
	#     ax.plot(X[my_members, 0], X[my_members, 1], 'w',
	#             markerfacecolor=col, marker='.')
	#     ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
	#             markeredgecolor='k', markersize=6)
	# ax.set_title('KMeans')
	# ax.set_xticks(())
	# ax.set_yticks(())
	# plt.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (
	#     t_batch, k_means.inertia_))
	# plt.show()
	# plt.savefig('0901_kmeans.png',dpi=75)
	return k_means_labels

def try_AP(X,preference):
	t0 = time.time()
	print t0
	af = AffinityPropagation(preference=preference).fit(X)
	t_batch = time.time() - t0
	print t_batch	
	
	cluster_centers_indices = af.cluster_centers_indices_
	labels = af.labels_

	n_clusters_ = len(cluster_centers_indices)

	print('Estimated number of clusters: %d' % n_clusters_)
	# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
	# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
	# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
	# print("Adjusted Rand Index: %0.3f"
	#       % metrics.adjusted_rand_score(labels_true, labels))
	# print("Adjusted Mutual Information: %0.3f"
	#       % metrics.adjusted_mutual_info_score(labels_true, labels))
	# print("Silhouette Coefficient: %0.3f"
	#       % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	# 循环为每个类标记不同的颜色
	for k, col in zip(range(n_clusters_), colors):
	    # labels == k 使用k与labels数组中的每个值进行比较
	    # 如labels = [1,0],k=0,则‘labels==k’的结果为[False, True]
	    class_members = labels == k
	    cluster_center = X[cluster_centers_indices[k]]    # 聚类中心的坐标
	    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
	    plt.plot(cluster_center[0], cluster_center[1], markerfacecolor=col,
	             markeredgecolor='k', markersize=14)
	    for x in X[class_members]:
	        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

	#plt.title('count：%d' % n_clusters_)#预测聚类中心个数
	plt.savefig('0901_AP.png',dpi=75)

if __name__ == '__main__':
	dist()