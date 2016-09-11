# -*- coding: utf-8 -*-
import networkx as nx
import time
import numpy
from mcl_clustering import networkx_mcl
import json
import logging


logging.basicConfig(level=logging.INFO,filename='./log/mcl.log',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S', filemode='a')
def load_graph(f, skip_rows=0):
    g = nx.Graph()
    with open(f) as fo:
        lines = fo.readlines()[skip_rows:]
    for line in lines:
        try:
            a = line.strip('\n').split(' ')
            nodex = a[0]
            nodey = a[1]
            #weight = float(a[4])+float(a[5])+float(a[6])*0.001
            #print nodex,nodey,weight
        except ValueError:
            continue
        g.add_edge(nodex, nodey,)
        #g.add_edge(nodex, nodey, weight=float(weight))

    return g


def removing_based_on_betweeness(g):
    init_ncomp = nx.number_connected_components(g)   #连通图
    curr_ncomp = init_ncomp
    while curr_ncomp <= init_ncomp:
        print '3'
        bws = nx.edge_betweenness_centrality(g, weight='weight')  #介数
        print '4'
        max_bw = max(bws.values())
        # Remove all of the edge with the highest centrality
        for nodes, bw in bws.iteritems():
            if bw == max_bw:
                g.remove_edge(*nodes)
        curr_ncomp = nx.number_connected_components(g)


def get_deg(g):
    adj = nx.adj_matrix(g)
    nodes = g.nodes()
    t = adj.sum(axis=1)
    return {node: t[i, 0] for i, node in enumerate(nodes)}


def get_modularity(g, init_deg, m):
    deg = get_deg(g)
    modularity = 0
    for comp in nx.connected_components(g):
        for node in comp:
            modularity += (deg[node] - init_deg[node] ** 2 / (2 * m))
    return modularity / (2 * m)


def gn(g):
    init_n = g.number_of_edges()
    print "Original graph has {} edges".format(init_n)
    if init_n == 0:
        return None
    gn0 = time.time()
    m = nx.adj_matrix(g).sum() / 2   #adj_martix邻接矩阵
    init_deg = get_deg(g)
    i = 1
    while g.number_of_edges():
        print '1'
        removing_based_on_betweeness(g)
        print '2'
        print i
        if i % 5 == 0:
            print "iter {} modularity {} number of edges {}"\
                .format(i, get_modularity(g, init_deg, m), g.number_of_edges())
        i += 1
    print "Max modularity: {}".format(get_modularity(g, init_deg, m))
    return nx.connected_components(g)

def mcl_cluster(G):
    t0 = time.time()
    M,cluster =  networkx_mcl(G, expand_factor = 2,
                   inflate_factor = 2,
                   max_loop = 10,
                   mult_factor = 1)
    t1 = time.time() - t
    print t1
    print type(M),type(cluster)
    f1 = open('mcl_m.txt','w')
    f1.write(M)
    f1.close()
    f2 = open('mcl_cluster.txt','w')
    f2.write(json.dumps(cluster))
    f2.close()


if __name__ == "__main__":
    t0=time.time()
    graph = load_graph("redis_dist.txt", ",")
    print graph.edges()
    t1 = time.time()-t0
    print 'load_graph:',t1
    mcl_cluster(graph)
    t2 = time.time()-1
    print 'mcl_cluster:',t2