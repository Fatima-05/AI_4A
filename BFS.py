class Node:
    def __init__(self,state,parent,actions):
        self.state = state
        self.parent=parent
        self.actions=actions
def actionSeq(graph,initial,goal):
    sol=[goal]
    currentP=graph[goal].parent
    while currentP!=None:
        sol.append(currentP)
        currentP=graph[currentP].parent
    sol.reverse()
    return sol        
def BFS():
    initial='D'
    goal='F'
    graph = { 'A': Node('A',None,['B','E','C']),
              'B': Node('B',None,['A','D','E']),
              'C': Node('C',None,['F','G','A']),
              'D': Node('D',None,['B','E']),
              'E': Node('E',None,['A','B','D']),
              'F': Node('F',None,['C']),
              'G': Node('G',None,['C'])
    }
    frontier=[initial]
    explored=[]
    while len(frontier)!=0:
        current = frontier.pop(0)
        explored.append(current)
        actions = graph[current].actions
        for child in actions:
            if child not in frontier and child not in explored:
                graph[child].parent=current
                if graph[child].state==goal:
                    return actionSeq(graph,initial,current)
                frontier.append(child)


if __name__ == "__main__":
    result = BFS()
    result.append('F')
    print(result)