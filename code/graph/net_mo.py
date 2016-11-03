import networkx as nx
def net_modu(partition, graph) :
    """Compute the modularity of a partition of a graph

    Parameters
    ----------
    partition : dict
       the partition of the nodes, i.e a dictionary where keys are their nodes and values the communities
    graph : networkx.Graph
       the networkx graph which is decomposed

    Returns
    -------
    modularity : float
       The modularity

    Raises
    ------
    KeyError
       If the partition is not a partition of all graph nodes
    ValueError
        If the graph has no link
    TypeError
        If graph is not a networkx.Graph

    References
    ----------
    .. 1. Newman, M.E.J. & Girvan, M. Finding and evaluating community structure in networks. Physical Review E 69, 26113(2004).

    Examples
    --------
    >>> G=nx.erdos_renyi_graph(100, 0.01)
    >>> part = best_partition(G)
    >>> modularity(part, G)
    """
    if type(graph) != nx.Graph :
        raise TypeError("Bad graph type, use only non directed graph")

    inc = dict([])
    deg = dict([])
    links = graph.size(weight='weight')
    #print links
    if links == 0 :
        raise ValueError("A graph without link has an undefined modularity")

    #print '1',deg
    for node in graph :
        com = partition[node]
        #print '2',deg
        #print com,node,deg.get(com, 0.),graph.degree(node, weight = 'weight') 
        deg[com] = deg.get(com, 0.) + graph.degree(node, weight = 'weight')   #
        #print '3',deg
        #print node,graph[node].items() 
        for neighbor, datas in graph[node].items() :
            #print neighbor,datas
            weight = datas.get("weight", 1)
            if partition[neighbor] == com :
                if neighbor == node :
                    inc[com] = inc.get(com, 0.) + float(weight)
                else :
                    inc[com] = inc.get(com, 0.) + float(weight)

    res = 0.
    print deg
    for com in set(partition.values()) :
    	#print inc,deg
    	#print inc.get(com, 0.),deg.get(com, 0.)
    	#print inc.get(com, 0.) / (links*2.)
        res += (inc.get(com, 0.) / (links*2.)) - (deg.get(com, 0.) / (2.*links))**2
    return res