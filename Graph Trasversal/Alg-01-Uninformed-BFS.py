"""
  This is the basic Breadth First Search algorithm also known as the BFS algorithm.
  It's main principle is finding the destination node, starting at the root node of a graph
by  
"""

from multiprocessing import process
import queue

def breadth_first_search(graph, start, end):
    
    """ 
    F A Z A - 1: 
        Failsafe u slucaju da je startni cvor start
        u stvari trazeni end cvor
    P H A S E - 1:
        A failsafe in case the starting node start 
        is the end node we're looking for
    """

    if start is end:
        path = list()
        path.append(start)
        return path
        
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found_dest = False

    """
    F A Z A - 2: 
        Glavna petlja koja prolazi kroz sva odredista cvorova u nadi 
        da ce naci krajnji cvor end i od njih formira recnik putanja
    
    P H A S E - 2: 
        The main loop that goes through every destination of a node 
        in the hopes of finding the ending node while forming a dictionary 
        that will be used to form a path from start to end
    """

    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        process(node)
        for dest in graph[node]:
           if dest not in visited:
            prev_nodes[dest] = node
            if dest is end:
                found_dest = True
                break
            visited.add(dest)
            queue_nodes.put(dest)

    """ 
    F A Z A - 3: 
        Formiranje putanje od starta 
        do trazenog cvora end u slucaju nalazenja 
        koriscenjem BFS algoritma 
    
    P H A S E - 3:
        Forming the path from the starting node 
        to the destination node in the case of finding it 
        through the BFS algorithm
    """

    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path