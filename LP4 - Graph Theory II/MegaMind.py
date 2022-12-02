"""
Igrac ima na raspolaganju 20 kuglica, 
od kojih su svake 4 iste boje.

Boje kuglica su bela, zuta, crvena, zelena i plava. 
Na pocetku igre 4 kuglice su proizvoljno rasporedjene 
na 4 mesta i poznat je izgled ciljne cetvorke kuglica.

Zadatak igraca je od pocetnog rasporeda kuglica dodje 
do ciljnog pri cemu u svakom koraku moze da zameni 
samo jednu kuglicu drugom.

Zapamtiti korake promene kuglica koje vode do cilja.
Zadatak je modifikacija poznate igre Master mind
"""


def megamind(start, goal):
    open_set = set()
    closed_set = set()
    prev_state = {}
    g = {}
    h = {}
    path = []

    store = {}
    store[start] = {
        'attempt': start,
        'used': start,
        'unused': str([i * (4 - start.count(i)) for i in ['w','y','r','g','b']])
    }

    end = False
    open_set.add(start)
    g[start] = 0
    h[start] = heuristics(store[start], goal)
    prev_state[start] = None

    while open_set and not end:
        state = None
        for next_state in open_set:
            h[next_state] = heuristics(store[next_state], goal)
            if state is None or g[next_state] + h[next_state] < g[state] + h[state]:
                state = next_state

        if state == goal:
            end = True
            break

        for ns in findNext(store[state]):
            store[ns['attempt']] = ns
            
            if ns['attempt'] not in open_set and ns['attempt'] not in closed_set:
                open_set.add(ns['attempt'])
                prev_state[ns['attempt']] = state
                h[ns['attempt']] = heuristics(ns, goal)
                g[ns['attempt']] = g[state] + 1

            elif g[ns['attempt']] > g[state] + h[ns['attempt']]:
                g[ns['attempt']] = g[state] + 1
                prev_state[ns['attempt']] = state
                if ns['attempt'] in closed_set:
                    closed_set.remove(ns['attempt'])
                    open_set.add(ns['attempt'])

        open_set.remove(state)
        closed_set.add(state)

    if end:
        prev = state
        while prev_state[prev] is not None:
            path = [prev] + path
            prev = prev_state[prev]
        path = [start] + path
    
    return path


#######################################################################################################


def findNext(state):
    newStates = []
    start = state['attempt']
    unused = state['unused']
    used = state['used']

    for f in unused:
        newStates += [
            {
                'attempt': f + start[1:],
                'unused': unused.replace(f, "", 1),
                'used': used + f
            },
            {
                'attempt': start[0] + f + start[2:],
                'unused': unused.replace(f, "", 1),
                'used': used + f
            },
            {
                'attempt': start[:2] + f + start[3],
                'unused': unused.replace(f, "", 1),
                'used': used + f
            },
            {
                'attempt': start[:3] + f,
                'unused': unused.replace(f, "", 1),
                'used': used + f
            }
        ]

    return list(filter(isValid, newStates))


#######################################################################################################


def isValid(state):
    return len(state['used']) <= 20


#######################################################################################################
    

def heuristics(state, skocko):
    val = 0
    for i in range(0,4):
        if state['attempt'][i]==skocko[i]:
            val+=5
        elif skocko[i] in state['attempt']:
            val +=1
    return len(state['used']) * 5 - val


#######################################################################################################

