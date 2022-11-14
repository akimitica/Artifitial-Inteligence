import queue
from multiprocessing import process

def depth_first_search(graph, start, end):
    
    """
    F A Z A - 1:
        ista kao za BFS

    P H A S E - 1:
        Same as BFS
    """

    if start is end:
        path = list()
        path.append(start)
        return path

    """
    F A Z A - 2:
        Slicna kao u BFS, jedina je razlika u tome sto umesto reda se koristi 
        magacin sto omogucava da obradjujemo cvorove po dubini, a ne prvo potomke

    P H A S E - 2:
        Very similar to the BFS algorithm, the difference being we use 
        a stack to store pending nodes for processing which allows us 
        to traverse nodes by depth and not by breadth
    """
    stack_nodes = set()
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False

    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        process(node)
        for dest in reversed(graph[node]):
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                stack_nodes.put(dest)

    """
    F A Z A - 3:
        Ista kao za BFS

    P H A S E - 3:
        Same as BFS
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