import math
class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost

def findMin (frontier) :
    minV=math.inf
    node=' '
    for i in frontier:
        if minV>frontier[i] [1] :
            minV=frontier [i] [1]
            node = i
    return node

def actionSeq(graph,initial,goal):
    sol=[goal]
    currentP=graph[goal].parent
    while currentP!=None:
        sol.append(currentP)
        currentP=graph[currentP].parent
    sol.reverse()
    return sol        
def UCS():
    initial='Arad'
    goal='Bucharest'
    graph = { 'Oradea': Node('Oradea',None,[('Zerind',71), ('Sibiu',151)],0),
        'Zerind': Node('Zerind',None,[('Oradea',71), ('Arad',75)],0),
        'Arad': Node('Arad',None,[('Zerind',75), ('Sibiu',140), ('Timisoara',118)],0),
        'Sibiu': Node('Sibiu',None,[('Oradea',151), ('Arad',140), ('Fagaras',99), ('Rimnicu Vilcea',80)],0),
        'Timisoara': Node('Timisoara',None,[('Arad',118), ('Lugoj',111)],0),
        'Fagaras': Node('Fagaras',None,[('Sibiu',99), ('Bucharest',211)],0),
        'Lugoj': Node('Lugoj',None,[('Timisoara',111),('Mehadia',70)],0),
        'Mehadia':Node('Mehadia',None,[('Lugoj',70),('Drobeta',75)],0),
        'Drobeta':Node('Drobeta',None,[('Mehadia',75),('Craiova',140)],0),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,[('Sibiu',80),('Pitesti',97),('Craiova',146)],0),
        'Craiova':Node('Craiova',None,[('Rimnicu Vilcea',146),('Drobeta',120),('Pitesti',138)],0),
        'Pitesti':Node('Pitesti',None,[('Rimnicu Vilcea',97),('Craiova',138),('Bucharest',101)],0),
        'Bucharest':Node('Bucharest',None,[('Pitesti',101),('Fagaras',211),('Giurgiu',90),('Urziceni',85)],0),
        'Giurgiu':Node('Giurgiu',None,[('Bucharest',90)],0),
        'Urziceni':Node('Urziceni',None,[('Bucharest',85),('Hirsova',98),('Vaslui',142)],0),
        'Hirsova':Node('Hirsova',None,[('Urziceni',98),('Eforie',86)],0),
        'Eforie':Node('Eforie',None,[('Hirsova',86)],0),
        'Vaslui':Node('Vaslui',None,[('Urziceni',142),('Iasi',92)],0),
        'Iasi':Node('Iasi',None,[('Vaslui',92),('Neamt',87)],0),
        'Neamt':Node('Neamt',None,[('Iasi',87),('Fagaras',211)],0)
    }
    frontier=dict()
    frontier[initial]=(None, 0)
    explored=[]
    while len(frontier)!=0:
        current=findMin(frontier)
        del frontier[current]
        if graph[current].state==goal:
            return actionSeq(graph,initial,goal)
        explored.append(current)

        for child in graph[current].actions:
            currentCost=child[1]+graph[current].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent=current
                graph[child[0]].totalCost=currentCost
                frontier[child[0]]=(graph[child[0]].parent,graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]] [1]<currentCost:
                    graph[child[0]].parent=frontier[child[0]] [0]
                    graph[child[0]].totalCost=frontier[child[0]] [1]
                else:
                    frontier[child[0]]=(current,currentCost)
                    graph[child[0]].parent=frontier[child[0]] [0]
                    graph[child[0]].totalCost=frontier[child[0]][1]


if __name__ == "__main__":
    result = UCS()
    print(result)