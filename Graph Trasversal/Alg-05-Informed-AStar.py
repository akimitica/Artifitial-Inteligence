
def AStar(graph, start, end):
    found_end = False
    open_set = set(start)
    closed_set = set()
    g={}
    prev_nodes = {}
    g[start] = 0
    prev_nodes[start] = None


    while len(open_set) > 0 and (not found_end):
        node = None
        for next_node in open_set:
            if node is None or g[next_node] + graph[next_node][0] < g[node] + graph[node][0]:
                node = next_node
        
        if node == end:
            found_end = True
            break

        
        for (m, cost) in graph[node][1]:
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                prev_nodes[m] = node
                g[m] = g[node] + cost
            else:
                if g[m] > g[node] + cost:
                    g[m] = g[node] + cost
                    prev_nodes[m] = node
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
        open_set.remove(node)
        closed_set.add(node)


    path = []
    price = 0
    if found_end:
        prev = end
        price+= g[end]
        while prev_nodes[prev] is not None:
            path.append(prev)
            price+=g[prev]
            prev = prev_nodes[prev]
        path.append(start)
        path.reverse()

    print(price)
    return path

graph = {
    "A": (9, [("B", 4), ("C", 6)]),
    "B": (6, [("D", 4), ("A", 2)]),
    "C": (2, [("D", 4), ("E", 1)]),
    "D": (2, [("E", 2), ("F", 3)]),
    "E": (3, [("F", 4)]),
    "F": (0, [("A", 1)])
}

print(AStar(graph, "A", "F"))