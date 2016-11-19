#-*-coding:utf-8-*-


import numpy as np
import pandas as pd
from na_copra import *
import collections,math


def attribute_sim(feat_name): #0-346
	attribute = pd.read_table(feat_name,delim_whitespace=True,header=None,index_col=0)
	att = attribute.as_matrix()   #计算余弦相似度作为相似度矩阵
	shape = att.shape[0]
	sim = np.zeros((shape,shape),np.float64)
	for i in range(shape):
		for j in range(i+1,shape):
			#print i,j,shape
			sim[i][j] = cosine_sim(att[i],att[j])
			sim[j][i] = sim[i][j]
	#print sim
	return sim,attribute.index[0]
	'''
	a_t = att.transpose()
	sim = np.dot(att,a_t)
	print sim   
	w_sim = sim/sim.max().astype('float64') #除最大的
	s_sim = w_sim - np.diag(w_sim.diagonal())  #对角线为0
	print sim.shape
	return s_sim #facebook属性相似度矩阵
	'''
def cosine_sim(i,j):
	return np.dot(i,j).astype('float64')/(np.sqrt(np.sum(i))+np.sqrt(np.sum(j))) #元素是1,0  不用平方


def standard_matrix(c):
	return (c-c.min(axis=1,keepdims=True))/(c.max(1)-c.min(1)).reshape(-1,1).astype('float64')   
	#reshape把[2,4,3]变成[[2],[4],[3]],   c除的时候第一行除以2，第二行除以4...，要是不reshape，就成了每行都除以[2,3,4]


def relation_deal(edge_name,vertics,ori_index):  #0-346
    f = open(edge_name,'r')
    lines = f.readlines()
    user_dict = collections.defaultdict(set)  #字典的建默认是个set
    for line in lines:
        users = line.strip().split(' ')
        user_dict[int(users[0])-ori_index].add(int(users[1])-ori_index)
        user_dict[int(users[1])-ori_index].add(int(users[0])-ori_index)
    matrix_friend = np.zeros((vertics,vertics),np.float64)
    matrix = np.zeros((vertics,vertics),np.float64)
    for k,v in user_dict.iteritems():
        #任意两用户的杰卡德
        for other_k,other_v in user_dict.iteritems():
            matrix_friend[k][other_k] = jaccard_similiar(v,other_v)
            matrix_friend[other_k][k] = matrix[k][other_k]
            if other_k in v:
                matrix[k][other_k] = matrix[other_k][k] = 1
        #两用户间有彼此的
        '''
        for j in v:
            matrix[k-1][j-1] = 1#jaccard_similiar(v,user_dict[j])
            matrix[j-1][k-1] = matrix[k-1][j-1]  #facebook无向，twitter有向
        '''
    return matrix_friend,matrix

def jaccard_similiar(set_i,set_j):
	return len(set_i.intersection(set_j))/float(len(set_i.union(set_j)))


def real_circles(circle_name):
	f = open(circle_name,'r')
	lines = f.readlines()
	circles = collections.defaultdict(list)
	for line in lines:
		element = line.strip('\n ').split('\t')
		circles[element[0]] = [int(i)-1 for i in element[1:] if len(i)>0]
	return circles


def relation_attribute(relation,attribute):
	nor_rel = relation/relation.max()
	nor_att = attribute/attribute.max()
	w1 = 0.6
	w2 = 1 - w1
	mask = nor_rel == 0
	nor_att[mask]=0
	mix_matrix = w1*nor_rel+w2*nor_att
	max_l=5 #最大可重复
	real_c = real_circles()
      #把mix矩阵中只传进去circle里有的点    不过这样的话索引位置？重新排点？
	getcoms(mix_matrix,len(mix_matrix),max_l,real_c)
	return mix_matrix

def tri_relation_attribute(m_friend,rel,att,circle_name):
    nor_fri = m_friend/m_friend.max()
    nor_rel = rel/rel.max()
    nor_att = att/att.max()
    sum_rel = rel.sum(axis=1)
    sort_rel = np.argsort(-sum_rel)
    w1 = 0.2
    w2 = 0.2
    w3 = 1-w1-w2
    print w1,w2,w3
    print 'w1*nor_fri+w2*nor_rel+w3*nor_att'
    mix_matrix = w1*nor_fri+w2*nor_rel+w3*nor_att
    max_l=[9,10,11,12] #最大可重复
    real_c = real_circles(circle_name)
    for m in max_l:
        print '    '
        print 'max vers:',m
        nmi = 0.0
        #for times in range(10):
        nmi += getcoms(mix_matrix,len(mix_matrix),m,real_c,sort_rel)  
        #print 'mean nmi:',nmi/10
    return mix_matrix


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
    
    
'''
1.读链接关系
2.计算链接关系相似度，作为权重，形成邻接矩阵
3.设置初始标签——问题：工作地方、生日这种标签每个人都是固有的，那传播的过程中也不好接受别人的标签    计算相似度？-->计算余弦相似度  
	相似度矩阵加权后，传播按什么传？要在拓扑关系的基础上考虑权重吗？还是没有拓扑关系也可以？
	还是先在拓扑的基础上传吧

4.从文本中提取主要内容作为标签传
5.对于每个点i：
	i的所有邻居节点j的标签和权重求和
	判断是否更新i的标签
	（问题：异步更新？）

'''

def why_sim():
    real_c = real_circles()
    att = attribute_sim()
    m_friend,rel = relation_deal()
    mix = tri_relation_attribute(m_friend,rel,att)
    print 'mean:',mean(mix)
    for k,v in real_c.iteritems():
        arv_sim = 0.0
        if len(v)>1:
            print 'circle:',k
            ave = mix[v[0]-1][v[-1]-1]
            arv_sim += ave
            #print 'sim:',v[0],v[-1],mix[v[0]-1][v[-1]-1]
            for i in range(len(v)-1):
#                try:
#                    #print 'sim:',v[i],v[i+1],mix[v[i]-1][v[i+1]-1]
#                except IndexError:
#                    pass
                arv_sim += mix[v[i]-1][v[i+1]-1]
            print arv_sim/len(v)
            print '============='


if __name__ == '__main__':  
    att,ori_index = attribute_sim('0.feat')
    m_friend,rel = relation_deal('0.edges',len(att),ori_index)
    #relation_attribute(rel,att)
    tri_relation_attribute(m_friend,rel,att,'0.circles')
    
#    why_sim()
    # result= {0: [10, 11, 14, 17, 32, 33, 34, 36, 41, 42, 46, 48, 51, 60, 69, 73, 80, 89, 96, 113, 119, 123, 137, 144, 152, 153, 154, 156, 159, 163, 178, 181, 182, 189, 191, 197, 204, 205, 208, 209, 214, 215, 232, 233, 239, 240, 243, 246, 252, 254, 255, 266, 278, 281, 285, 286, 291, 293, 300, 304, 315, 334], 66: [0, 2, 4, 6, 8, 9, 12, 15, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 35, 37, 38, 39, 44, 47, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 68, 71, 72, 74, 75, 76, 78, 79, 81, 82, 83, 84, 86, 87, 91, 93, 95, 97, 99, 100, 102, 103, 104, 105, 106, 107, 108, 112, 116, 117, 118, 120, 121, 122, 124, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 138, 140, 141, 145, 147, 149, 155, 157, 158, 160, 162, 164, 167, 168, 169, 170, 171, 175, 177, 179, 183, 184, 185, 186, 187, 188, 190, 193, 195, 196, 198, 199, 202, 203, 206, 207, 210, 211, 212, 216, 220, 221, 222, 223, 227, 228, 230, 231, 234, 235, 236, 237, 238, 241, 245, 247, 248, 249, 250, 251, 253, 256, 257, 259, 260, 264, 265, 267, 268, 269, 270, 271, 273, 275, 276, 279, 280, 282, 283, 284, 287, 289, 290, 294, 296, 297, 298, 299, 301, 302, 303, 307, 308, 310, 312, 313, 314, 316, 317, 319, 321, 322, 323, 324, 328, 329, 330, 331, 333, 335, 337, 338, 339, 340, 341, 343, 344, 345, 346], 201: [201, 172, 165], 311: [1, 13, 16, 18, 19, 22, 27, 31, 40, 43, 70, 92, 110, 111, 114, 115, 136, 139, 143, 148, 150, 161, 166, 173, 213, 219, 225, 229, 242, 261, 288, 292, 306, 309, 311, 325, 332, 336, 342], 226: [22, 45, 67, 85, 98, 101, 130, 142, 174, 176, 224, 226, 262, 277, 295, 320], 274: [3, 77, 151, 180, 194, 217, 272, 274, 305, 327], 172: [], 258: [7, 90, 109, 192, 200, 244, 258, 263], 318: [5, 88, 94, 146, 218, 318, 326]}
    # c = {'circle3': [51, 83, 237], 'circle2': [155, 99, 327, 140, 116, 147, 144, 150, 270], 'circle1': [173], 'circle0': [71, 215, 54, 61, 298, 229, 81, 253, 193, 97, 264, 29, 132, 110, 163, 259, 183, 334, 245, 222], 'circle7': [225, 46], 'circle6': [337, 289, 93, 17, 111, 52, 137, 343, 192, 35, 326, 310, 214, 32, 115, 321, 209, 312, 41, 20], 'circle5': [23], 'circle4': [125, 344, 295, 257, 55, 122, 223, 59, 268, 280, 84, 156, 258, 236, 250, 239, 69], 'circle9': [336, 204, 74, 206, 292, 146, 154, 164, 279, 73], 'circle8': [282], 'circle22': [267], 'circle23': [28, 149, 162], 'circle20': [244, 282, 262, 293, 220, 174], 'circle21': [12], 'circle17': [90, 52, 172, 126, 294, 179, 145, 105, 210], 'circle16': [251, 94, 330, 5, 34, 299, 254, 24, 180, 194, 281, 101, 266, 135, 197, 173, 36, 9, 85, 57, 37, 258, 309, 80, 139, 202, 187, 249, 58, 127, 48, 92], 'circle15': [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316, 96, 246, 347, 121, 7, 3, 170, 323, 56, 338, 23, 109, 141, 67, 345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26, 31, 168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233, 1, 294, 280, 224, 269, 256, 60, 328, 189, 146, 77, 196, 64, 286, 89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291, 21, 315, 261, 47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103, 157, 277, 105, 139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152, 236, 308, 82, 87, 136, 200, 183, 247, 290, 303, 319, 6, 314, 104, 127, 25, 69, 171, 119, 79, 340, 301, 188, 142], 'circle14': [175, 227], 'circle13': [138, 131, 68, 143, 86], 'circle12': [278], 'circle11': [324, 265, 54, 161, 298, 76, 165, 199, 203, 13, 66, 113, 97, 252, 313, 238, 158, 240, 331, 332, 134, 218, 118, 235, 311, 151, 308, 212, 70, 211], 'circle10': [42, 14, 216, 2], 'circle19': [93, 33, 333, 17, 137, 44, 343, 326, 214, 115, 312, 41, 20], 'circle18': [177]}
    #dict_a = {'1': [0, 1, 2, 3, 4, 5], '3': [12, 13, 14, 15, 16], '2': [6, 7, 8, 9, 10, 11]}
    #dict_b = {'1': [0, 2, 3, 4, 5, 6, 12, 13], '3': [11, 14, 15, 16], '2': [1, 7, 8, 9, 10]}

    #dict_a = {'1': [0, 1, 2, 3, 4, 5], '3': [12, 13, 14, 15, 16], '2': [6, 7, 8, 9, 10, 11]}
    #dict_b = {'1': [0],'4':[1, 2],'5':[3],'6':[4, 5], '3': [12, 13, 14, 15, 16], '2': [6, 7, 8, 9, 10, 11]}
    #print na_nmi(dict_a, dict_b, 17)
