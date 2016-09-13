# -*- coding: utf-8 -*-
import time
from igraph import *
from gn import load_graph
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
#import fix_clustering
from relation_mongo2redis import cal_modularity,e_modularity
from cluster_jln import try_kmeans,try_AP
import logging 

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,filename='./log/9010_kmeans.log',filemode='a')
#logger = logging.getLogger(__name__)

def try_igraph():
    time0=time.time()
    graph = load_graph("redis_dist.txt",is_weight=True)
    #g = Graph()
    #g.add_vertices(graph.nodes())
    #g.add_edges(graph.edges())
    read_list = []
    for n,nbrs in graph.adjacency_iter():#把network的graph按 source,target,weight存起来
        for nbr,eattr in nbrs.items():
            read_list.append([n,nbr,eattr['weight']])

    g = Graph.TupleList(read_list,weights=True)
    print 'generate graph:',time.time()-time0
    logging.info("generate graph spend %s seconds" % str(time.time()-time0))
    #use igraph methods
    #methods = ['multilevel','fastgreedy','walktrap','spinglass','edge_betweenness']
    methods = ['multilevel'] #multilevel没有子类？没有clusters  'spinglass'----太慢了   'multilevel',也不能用这个
    for i in methods:
        igraph_cls = clustering(g,i)
        t3 = time.time()
        a = cal_modularity(g.get_adjacency().data,[i for i in igraph_cls])#[i for i in clusters]---igraph result   ///cluster for kmeans resulte
        print 'modularity:',time.time()-t3
        #f.write(str(i)+' modularity:'+str(a))
        logging.info("%s self_modularity: %s " % (str(i),a))
        print 'self_modularity:',a
        '''
        #use kmeans
        time1 = time.time()
        for i in range(3,12):
            labels = use_dist(i)
            print 'kmeans:',time.time()-time1
            logging.info("%s kmeans spend %s seconds" % (str(i),time.time()-time0))


            t2 = time.time()
            cluster_dict = {}
            for index, cluster in enumerate(labels):
                try:
                    cluster_dict[cluster].append(index)
                except:
                    cluster_dict[cluster] = [index]
            clusters = []
            f = open('0910_kmeans.txt','a')
            f.write(str(i)+'\n')
            for dots in cluster_dict.values():
                clusters.append(dots)
                f.write(str(dots)+'\n')
            print cluster_dict
            print 'write clusters:',time.time()-t2
            logging.info("clusters: %s " % str(cluster_dict))
        '''
        # for cluster in cl:
        #     print " ".join(str(idx) for idx in cluster)
        #plot(g,'big.png')
        #clustering(g)
    logging.info('===================end=====================')

def clustering(graph,i):
 
    #methods = ['walktrap','multilevel','fastgreedy','edge_betweenness'] #multilevel没有子类？没有clusters  'spinglass'----太慢了
    #for i in methods:
    print "\n# "+i+" Clustering:"
    logging.info("%s Clustering: " % i)
    t0 = time.time()
    method = eval('graph.community_'+i+'(weights="weight",return_levels=True)') #,return_levels=True
    dendrograms = method
    #dendrogram = method
    #logging.info("return_levels=True:" % dendrogram)
    #为了multilevel显示迭代次数
    for i in range(len(dendrograms)):
        logging.info("---the %s Iters ---" % i)
        clusters = dendrograms[i]
        print "--- Clustering found %s clusters ---" % len(clusters)
        logging.info("--- Clustering found %s clusters ---" %  len(clusters))
        for j in range(len(clusters)):
            logging.info("%s clusters members: %s" % (j,clusters[j]))
        logging.info("modularity: %s" % clusters.modularity)
    
    # try:
    #     clusters = dendrogram.as_clustering()
    # except:
    #     clusters = dendrogram
    # print "---"+i+" Clustering found %s clusters ---" % len(clusters)
    # logging.info("---%s Clustering found %s clusters ---" % (i, len(clusters)))
    
        # try:
        #     fix_dendrogram(graph, dendrogram)
        #     clusters = dendrogram.as_clustering()
        #     print "---"+i+" Clustering found %s clusters ---" % len(clusters)
        #     logging.info("---%s Clustering found %s clusters ---" % (i, len(clusters)))
        # except:
        #     pass
    # try:
    #     print clusters.modularity
    #     for i in range(len(clusters)):
    #         logging.info("%s clusters members: %s" % (i,clusters[i]))
    #     logging.info("modularity: %s" % clusters.modularity)
    # except:
    #     clusters = []
    t1 = time.time() - t0
    print 'time spend:'+ str(t1)
    logging.info("time spend : %s" % str(t1))
    # plot_graph(graph,clusters,i)
    # t2 = time.time() - t1
    # print 'draw_time:'+ str(t2)
    #print clusters
    return clusters


def plot_graph(graph,clusters,name):
    color_list = ['red','blue','yellow','green','darkblue','brown','black','pink','grey','orange','purple','lightblue','white']
    for i in range(0,len(clusters)):
        seq = graph.vs.select(clusters[i])
        seq['color'] = color_list[i]
        #seq['color'] = pal.get(i) #pal.get(i)
    #print graph.vs['color']
    plot(graph,name+'.png')


def fix_dendrogram(graph, cl):
    already_merged = set()
    for merge in cl.merges:
        already_merged.update(merge)

    num_dendrogram_nodes = graph.vcount() + len(cl.merges)
    not_merged_yet = sorted(set(xrange(num_dendrogram_nodes)) - already_merged)
    if len(not_merged_yet) < 2:
        return

    v1, v2 = not_merged_yet[:2]
    cl._merges.append((v1, v2))
    del not_merged_yet[:2]

    missing_nodes = xrange(num_dendrogram_nodes,
                           num_dendrogram_nodes + len(not_merged_yet))
    cl._merges.extend(izip(not_merged_yet, missing_nodes))
    cl._nmerges = graph.vcount()-1



def test(graph):
    graph = Graph.Famous("Zachary")
    # print "\n# edge_betweennes Clustering:"
    # dendrogram = graph.community_edge_betweennes()
    # clusters = dendrogram.as_clustering()
    # print "---edge_betweennes Clustering found %s clusters ---" % len(clusters)
    # print clusters.modularity


    #membership = [[0, 1, 3, 7, 11, 12, 17, 19, 21],[2, 8, 9, 13, 28, 30, 31],[4, 5, 6, 10, 16],\
    #               [14, 15, 18, 20, 22, 26, 29, 32, 33],[23, 24, 25, 27]]
    #print graph.modularity(membership=membership)
    #print graph.modularity(membership=[[0, 1, 3, 7, 11, 12, 17, 19, 21],[2, 8, 9, 13, 28, 30, 31],[4, 5, 6, 10, 16],[14, 15, 18, 20, 22, 26, 29, 32, 33],[23, 24, 25, 27]])

    print "\n# Walktrap Clustering:"
    dendrogram = graph.community_walktrap()
    clusters = dendrogram.as_clustering()
    print "---Walktrap Clustering found %s clusters ---" % len(clusters)
    print clusters
    print clusters.modularity


    a = cal_modularity(graph.get_adjacency().data,[i for i in clusters])

    #b = e_modularity(graph.get_adjacency().data,[i for i in clusters])
    #plot_graph(clusters)
    pal = ClusterColoringPalette(n=100)#RainbowPalette
    #color_list = ['red','blue','yellow','green','darkblue','brown','black','pink','grey','orange','purple','lightblue','white']
    # for i in range(0,len(clusters)):
    #     print clusters[i]
    #     seq = graph.vs.select(clusters[i])
    #     seq['color'] = color_list[i]
        #seq['color'] = pal.get(i) #pal.get(i)
    #print graph.vs['color']
    plot(clusters,'famous.png',palette = pal)   
    #a = cut(graph,membership)


if __name__ == '__main__':
    try_igraph()
    #clustering()
    #test()