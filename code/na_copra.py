# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:55:54 2016

@author: NaNa
"""

from numpy import *
import networkx as nx
import time
import copy
from basics import load_graph,plot_graph,ng_to_ig
import numpy as np
import igraph 



def Degree_Sorting(Adjmartrix,vertices):
    degree_s = [[i,0] for i in range(vertices)]
    neighbours = [[] for i in range(vertices)]
    sums = 0
    for i in range(vertices):
        for j in range(vertices):
            if Adjmartrix[i][j] == 1:
                degree_s[i][1] += 1
                sums += 1
                neighbours[i].append(j)
                #degree_s = sorted(degree_s, key=lambda x: x[1], reverse=True)
    #print degree_s,neighbours,sums/2
    return degree_s,neighbours,sums/2

def Propagate(x,old, new, neighbours,v,asynchronous):
    new[x] = {}
    #洗牌保证随机性（都相等的情况）
    random.shuffle(neighbours)
    #print 'neighbours',neighbours
    #依据邻结点标签集更新该节点
    for eachpoint in neighbours:   #对于节点的每个邻居
        for eachlable in old[eachpoint]:   #这个邻居在之前表里有的点
            b = old[eachpoint][eachlable]      #53 23 55  代表标签
            #print 'b',b
            if eachlable in new[x]:
                new[x][eachlable] += b    #标签
            else:
                new[x].update({eachlable: b})   
            if asynchronous:
                old[x] = copy.deepcopy(new[x])
    Normalize(new[x])
    #print new[x]
    maxb = 0.0
    maxc = 0
    t = []
    #去除小于1/v的候选项，若均小于则''选b最大的赋值''，否则规范化
    for each in new[x]:
        if new[x][each] < 1/float(v):
            t.append(each)
            if new[x][each] >= maxb:#取最后一个
            #if new[x][each] > maxb:#取第一个
                maxb = new[x][each]
                maxc = each
    for i in range(len(t)):
        del new[x][t[i]]
    if len(new[x]) == 0:
        new[x][maxc] = 1
    else:
        Normalize(new[x])

def Normalize(x):
    sums = 0.0
    for each in x:
        sums += x[each]
    for each in x:
        if sums != 0:
            x[each] = x[each]/sums

def id_l(l):
    ids = []
    for each in l:
        ids.append(id_x(each))
    return ids

def id_x(x):
    ids = []
    for each in x:
        ids.append(each)
    return ids

def count(l):
    counts = {}
    for eachpoint in l:
        for eachlable in eachpoint:
            if eachlable in counts:
                n = counts[eachlable]
                counts.update({eachlable: n+1})
            else:
                counts.update({eachlable: 1})
    return counts

def mc(cs1, cs2):
    #print cs1,cs2
    cs = {}
    for each in cs1:
        if each in cs2:
            cs[each] = min(cs1[each], cs2[each])
    return cs

def Modulartiy(A, coms, sums,vertices):
    Q = 0.0
    for eachc in coms:
        li = 0
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                li += A[eachp][eachq]
        li /= 2
        di = 0
        for eachp in coms[eachc]:
            for eachq in range(vertices):
                di += A[eachp][eachq]
        Q = Q + (li - (di * di) /(sums*4))
    Q = Q / float(sums)
    return Q
'''
def ExtendQ(A,coms,sums,k,o):
    #k-每个节点的度数 o-每个节点属于的社区数
    EQ = 0.0
    for eachc in coms:
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                EQ += (A[eachp][eachq] - k[eachp][1]*k[eachq][1]/(2*sums)) / (o[eachp]*o[eachq])
    EQ = EQ / float(2*sums)
    return EQ
'''
def ExtendQ(A,coms,sums,k,o):
    #k-每个节点的度数 o-每个节点属于的社区数
    s = float(2*sums)
    k = sorted(k, key=lambda x: x[0], reverse=False)
    at = 0
    kt = 0
    EQ = 0.0
    for eachc in coms:
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                at += A[eachp][eachq] / float(o[eachp]*o[eachq])
                kt += k[eachp][1]*k[eachq][1] / float(o[eachp]*o[eachq])
    EQ = at - kt / s
    return EQ/s


def getcoms(A,vertices,v,real_c):
    label_new = [{} for i in range(vertices)]
    label_old = [{i: 1} for i in range(vertices)]
    minl = {}
    oldmin = {}
    flag = True# asynchronous
    itera = 0# 迭代次数
    start = time.clock()# 计时
    #同异步迭代过程
    while True:   
        '''
        if flag:
            flag = False
        else:
            flag = True
        '''
        itera += 1
        for i in range(vertices):
            neighbours = np.where(A[i]>0)[0]
            Propagate(i,label_old, label_new, neighbours, v, flag)
        if id_l(label_old) == id_l(label_new):
            minl = mc(minl, count(label_new))
        else:
            minl = count(label_new)
        if minl != oldmin:
            label_old = label_new
            oldmin = minl
        else:
            break
    #print itera,label_old
    coms = {}
    sub = {}
    for each in range(vertices):
        ids = id_x(label_old[each])
        for eachc in ids:
            if eachc in coms and eachc in sub:
                coms[eachc].append(each)
            #elif :
                sub.update({eachc: set(sub[eachc]) & set(ids)})
            else:
                coms.update({eachc:[each]})
                sub.update({eachc:ids})
    #print 'lastiter',coms   #画图
    #获取每个节点属于的标签数
    o = [0 for i in range(vertices)]
    for eachid in range(vertices):
        for eachl in coms:
            if eachid in coms[eachl]:
                o[eachid] += 1         
    #去重取标签
    for each in sub:
        if len(sub[each]):
            for eachc in sub[each]:
                if eachc != each:
                    coms[eachc] = list(set(coms[eachc]) - set(coms[each]))
    #标签整理    
    clusterment = [0 for i in range(vertices)]
    a = 0
    for eachc in coms:   #社区的键
        if len(coms[eachc])!=0:
            for e in coms[eachc]:
                clusterment[e] = a + 1  #每个点出现在几个社区中
            a += 1
    #degree_s = sorted(degree_s, key=lambda x: x[0], reverse=False)
    elapsed = (time.clock() - start)
    print 't=',elapsed
    print 'result=',coms
    print 'clusterment=',clusterment
    print 'Q =',Modulartiy(A, coms, A.sum(),vertices)
    #print 'EQ =',ExtendQ(A,coms,sums,degree_s,o)
    print 'NMI=',NMI(coms,real_c,vertices)
    return coms



def NMI(cluA,cluB,vertices):
    #混淆矩阵
    cmat = [[0 for i in range(len(cluB))] for j in range(len(cluA))]
    i = 0
    j = 0
    for eacha in cluA:
        for eachb in cluB:
            cmat[i][j] = len(set(cluA[eacha]) & set(cluB[eachb]))
            j += 1
        i += 1
        j = 0     
    #the nmi_numerator part
    print cmat
    print len(cluA),len(cluB)
    nmi_numerator = 0.0
    for i in range(len(cluA)):
        for j in range(len(cluB)):
            if (cmat[i][j]!=0):
                row = 0
                column = 0
                for k in range(len(cluB)):
                    row = row + cmat[i][k]
                for l in range(len(cluA)):
                    column = column + cmat[l][j]
                nmi_numerator = nmi_numerator + cmat[i][j] * np.log2((cmat[i][j] * vertices)/float(row * column))
                
    nmi_numerator = -2 * nmi_numerator
    #the denominator part
    nmi_denominator1 = 0.0
    nmi_denominator2 = 0.0
    nmi = 0.0
    for i in range(len(cluA)):
        row = 0
        for k in range(len(cluB)):
            row = row + cmat[i][k]
        if(row != 0):
            nmi_denominator1 = nmi_denominator1 + row * np.log2(row / float(vertices))
    for j in range(len(cluB)):
        column = 0
        for l in range(len(cluA)):
            column = column + cmat[l][j];
        if(column != 0):
            nmi_denominator2 = nmi_denominator2 + column * np.log2(column / float(vertices))
    nmi_denominator = nmi_denominator1 + nmi_denominator2
    print nmi_numerator,nmi_denominator
    if(nmi_denominator != 0):
        nmi = nmi_numerator/float(nmi_denominator)
    print 'nmi',nmi
    return nmi


def BER(result_c,right_c): #Balanced Error Rate
	pass
	#http://i.stanford.edu/~julian/pdfs/nips2012.pdf


if __name__ == '__main__':
    #节点个数,V
    #vertices = [34,115,105,62]
    #txtlist = ['karate.txt','football.txt','books.txt','dolphins.txt']
    
    graph = load_graph("/home/jiangln/own_weibo/raw_data/facebook/0.edges",split_symbol=' ',is_weight=False)
    Adj =nx.adjacency_matrix(graph) 
    A = np.array(Adj.todense())
    ver = graph.number_of_nodes()
    degree_s, neighbours, sums = Degree_Sorting(A,ver)
    #print 'degree_s',degree_s
    #print 'neighbours',neighbours
    print 'sums',sums
    ev = 4  #可重复的标签数
    coms = getcoms(degree_s, neighbours, sums,A,ev,ver)
    com_list = [c for c in coms.values()]
    ig = ng_to_ig(graph)
    plot_graph(ig,com_list,'faceboo')  

    '''
    graph = igraph.Graph.Famous('Zachary')
    vertices = [34]
    txtlist = ['zachary.txt']
    testv = [5]
    coms = ''
    for i in range(len(txtlist)):
        print txtlist[i],vertices[i]
        for ev in testv:
            print 'v=',ev
            A = LoadAdjacentMatrixData(txtlist[i],vertices[i])
            degree_s, neighbours, sums = Degree_Sorting(A,vertices[i])
            #print neighbours
            coms = getcoms(degree_s, neighbours, sums,A,ev,vertices[i])
    com_list = [c for c in coms.values()]
    plot_graph(graph,com_list,'faceboo')
    '''
