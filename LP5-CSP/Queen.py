"""Implementirati Backtracking traženje 
u kombinaciji sa Forward checking tehnikom i MVR
heuristikom za raspoređivanje kraljica na šahovskoj tabli 
dimenzije 8x8 tako da se ne napadaju."""

def NQueen(n: int):
    solved = False

    initialState={
        'assigned': {},
        'nonAssignedAndDomains': { i:[j for j in range(1, n + 1)] for i in range(1, n + 1)}
    }

    stateStack = [initialState]
    finalState = None

    while not solved and stateStack:
        currentState = stateStack.pop(0)
        mrv = n
        currentNode = None
        for nonAssigned in list(currentState['nonAssignedAndDomains'].keys()):
            if len(currentState['nonAssignedAndDomains'][nonAssigned]) <= mrv:
                currentNode = nonAssigned
        
        for value in currentState['nonAssignedAndDomains'][currentNode]:
            nextState = {
                'assigned': {key:currentState['assigned'][key] for key in list(currentState['assigned'].keys())},
                'nonAssignedAndDomains': {i:[j for j in currentState['nonAssignedAndDomains'][i]] for i in list(currentState['nonAssignedAndDomains'].keys())}
            }
            ok = True

            for i in range(1, n + 1):
                if i != currentNode and i in list(nextState['nonAssignedAndDomains'].keys()):
                    if value in nextState['nonAssignedAndDomains'][i]:
                        nextState['nonAssignedAndDomains'][i].remove(value)
                    if value - currentNode + i in nextState['nonAssignedAndDomains'][i]:
                        nextState['nonAssignedAndDomains'][i].remove(value - currentNode + i)
                    if value + currentNode - i in nextState['nonAssignedAndDomains'][i]:
                        nextState['nonAssignedAndDomains'][i].remove(value + currentNode - i)

            nextState['nonAssignedAndDomains'].pop(currentNode)
            nextState['assigned'][currentNode] = value

            if len(nextState['assigned']) == n:
                solved = True
                finalState = nextState
                break
                
            for nonAssigned in list(nextState['nonAssignedAndDomains'].keys()):
                if len(nextState['nonAssignedAndDomains'][nonAssigned]) == 0:
                    ok = False
                    break

            if ok:
                stateStack.insert(0,nextState)
        
    if not solved:
        print('Failed')
    else:
        for i in range(1, n + 1):
            str=''
            pos = finalState['assigned'][i]
            for j in range(1, n + 1):
                if j!=pos:
                    str+='0'
                else:
                    str+='1'
            print(str)


NQueen(8)