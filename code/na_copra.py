# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:55:54 2016

@author: NaNa
"""

from numpy import *
import time
import copy
import numpy as np



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

def Propagate(x,old, new, neighbours,nei_weights,v,asynchronous):
    new[x] = {}
    #洗牌保证随机性（都相等的情况）  现在是按权重排序的
    #random.shuffle(neighbours)
    #print 'neighbours',neighbours
    #依据邻结点标签集更新该节点
    for eachpoint in neighbours:   #对于节点的每个邻居
        for eachlable in old[eachpoint]:   #这个邻居在之前表里有的点
            b = old[eachpoint][eachlable]      #53 23 55  代表标签
            #print 'b',b
            if eachlable in new[x]:
                new[x][eachlable] += b*nei_weights[eachpoint]    #标签
            else:
                new[x].update({eachlable: b*nei_weights[eachpoint]})   
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
                try:
                    li += A[eachp][eachq]
                except:
                    pass
        li /= 2
        di = 0
        for eachp in coms[eachc]:
            for eachq in range(vertices):
                try:
                    di += A[eachp][eachq]
                except:
                    pass
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


def deal_c(circle,mix,sort_rel):
    c_set = set()    
    for c_v in circle.values():
        for c_j in c_v:
            c_set.add(c_j)
    c_list = list(c_set)
    circle_new = {}
    for k,v in circle.iteritems():
        circle_new[k]=[c_list.index(j) for j in v]
    
    mix_new=mix[c_list][:,c_list]
    new_rel = [c_list.index(i) for i in sort_rel if i in c_list]    
    return circle_new,mix_new,len(c_list),new_rel

def getcoms(A,vertices,v,real_c,sort_rel):
    real_c,A,vertices,sort_rel = deal_c(real_c,A,sort_rel)
    range_list = range(vertices)
    label_new = [{} for i in range_list]
    label_old = [{i: 1} for i in range_list]
    minl = {}
    oldmin = {}
    flag = False# asynchronous
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
        vers = copy.deepcopy(range_list)
        for i in sort_rel:
            #i = random.choice(vers)
            neighbours = np.argsort(-A,axis=1)[i,:v]
            Propagate(i,label_old, label_new, neighbours,A[i], v, flag)
            vers.remove(i)
        '''
        for i in range(vertices):
            neighbours = np.argsort(-A,axis=1)[i,:v]
            Propagate(i,label_old, label_new, neighbours,A[i], v, flag)
        '''
        if id_l(label_old) == id_l(label_new):
            minl = mc(minl, count(label_new)) #统计每个标签出现的次数
        else:
            minl = count(label_new)
        if minl != oldmin:
            label_old = label_new
            oldmin = minl
        else:
            break
    print 'iter:',itera
    coms = {}
    sub = {}
    for each in range_list:
        ids = id_x(label_old[each])
        for eachc in ids:
            if eachc in coms and eachc in sub:
                coms[eachc].append(each)
            #elif :
                sub.update({eachc: set(sub[eachc]) & set(ids)})
            else:
                coms.update({eachc:[each]})
                sub.update({eachc:ids})

    elapsed = (time.clock() - start)
    print 't=',elapsed
    print 'counts=',len(coms.keys())
    #print 'result=',coms
    #print 'clusterment=',clusterment
    print 'Q =',Modulartiy(A, coms, A.sum(),len(range_list))
    #print 'EQ =',ExtendQ(A,coms,sums,degree_s,o)
    nmi = na_nmi(coms,real_c,len(range_list))    
    print 'NMI=',nmi
    #print label_old
    return nmi



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

def na_nmi(a,b,vertics):
    info = 0.0
    for i in a.keys():
        for j in b.keys():
            inter = len(set(a[i])&set(b[j]))
            if inter != 0:
                a1 = (float(inter)*vertics)/(len(a[i])*len(b[j]))
                b1 = math.log(a1,2)*(float(inter)/vertics)
                info += b1
    h = 0.0
    for dicts in [a,b]:
        for k in dicts.keys():
            if len(dicts[k]) != 0:
                p = float(len(dicts[k]))/vertics
                h += - p*(math.log(p,2))
    nmi = info*2/h
    return round(nmi,3)

    
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
