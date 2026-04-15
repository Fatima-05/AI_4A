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
    initial='Arad'
    goal='Bucharest'
    graph = { 'Oradea': Node('Oradea',None,['Zerind', 'Sibiu']),
        'Zerind': Node('Zerind',None,['Oradea', 'Arad']),
        'Arad': Node('Arad',None,['Zerind', 'Sibiu', 'Timisoara']),
        'Sibiu': Node('Sibiu',None,['Oradea', 'Arad','Fagaras','Rimnicu Vilcea']),
        'Timisoara': Node('Timisoara',None,['Arad', 'Lugoj']),
        'Fagaras': Node('Fagaras',None,['Sibiu','Bucharest']),
        'Lugoj': Node('Lugoj',None,['Timisoara','Mehadia']),
        'Mehadia':Node('Mehadia',None,['Lugoj','Drobeta']),
        'Drobeta':Node('Drobeta',None,['Mehadia','Craiova']),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti','Craiova']),
        'Craiova':Node('Craiova',None,['Rimnicu Vilcea','Drobeta','Pitesti']),
        'Pitesti':Node('Pitesti',None,['Rimnicu Vilcea','Craiova','Bucharest']),
        'Bucharest':Node('Bucharest',None,['Pitesti','Fagaras','Giurgiu','Urziceni']),
        'Giurgiu':Node('Giurgiu',None,['Bucharest']),
        'Urziceni':Node('Urziceni',None,['Bucharest','Hirsova','Vaslui']),
        'Hirsova':Node('Hirsova',None,['Urziceni','Eforie']),
        'Eforie':Node('Eforie',None,['Hirsova']),
        'Vaslui':Node('Vaslui',None,['Urziceni','Iasi']),
        'Iasi':Node('Iasi',None,['Vaslui','Neamt']),
        'Neamt':Node('Neamt',None,['Iasi'])
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
    result.append('Bucharest')
    print(result)