#   Dodati polazni cvor na stek
#   dodati polazni cvor u posecene
#   Dodati da polazni cvor nema prethodnika
#   Sve dok ciljni cvor nije pronadjen, a stek nije prazan:
#       Procitati cvor iz steka
#       Obraditi cvor
#       Za svaki odredisni cvor do kog postoji poteg od cvora dodati par u listu odrediste sa heuristikom
#       




from multiprocessing import process
import queue

def hill_climbing_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path

    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False

    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        process(node)
        destinations = list()
        for dest in graph[node][1]:
            element = {graph[dest][0], dest}
            destinations.append(element)
            for dest_heur in sorted(destinations, reverse = True):
                if dest_heur[1] not in visited:
                    prev_nodes[dest_heur[1]] = node
                    if dest_heur[1] is end:
                        found_dest = True
                        break
                    visited.add(dest_heur[1])
                    stack_nodes.put(dest_heur[1])
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path