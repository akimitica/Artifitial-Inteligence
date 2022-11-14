import queue
from multiprocessing import process

def best_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    
    priority_queue = queue()
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    priority_queue.put((graph[start][0],start))
    found_dest = False

    while (not found_dest) and (not priority_queue.empty()):
        node = priority_queue.get()
        process(node[1])
        for dest in graph[node[1]][1]:
            if dest not in visited:
                prev_nodes[dest] = node[1]
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                priority_queue.put((graph[dest][0],dest))
    
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path