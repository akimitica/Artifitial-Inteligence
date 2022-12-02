import queue

def breadth_first_search(graph, start):    
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    visited.add(start)
    queue_nodes.put(start)
    queue_nodes.put(1)

    while (not queue_nodes.empty()):
        node = queue_nodes.get()
        if (type(node) in {int}):
            if (queue_nodes.empty()):
                return node
            else:
                queue_nodes.put(node + 1)
        else:
            for dest in graph[node]:
                if dest not in visited:
                    visited.add(dest)
                    queue_nodes.put(dest)

                    

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : ['G', 'I'],
    'F' : ['J'],
    'G' : ['J'],
    'H' : [],
    'I' : ['J'],
    'J' : []
}

print(breadth_first_search(graph, 'A'))