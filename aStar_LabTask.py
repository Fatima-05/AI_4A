import math
class Node:
    def __init__(self,state,parent,actions,heuristic,totalCost):
        self.state = state
        self.parent=parent
        self.actions=actions
        self.heuristic=heuristic
        self.totalCost=totalCost

def findMin (frontier) :
    minV=math.inf
    node=' '
    for i in frontier:
        if minV>frontier[i] [1] :
            minV=frontier [i] [1]
            node=i
    return node

def actionSeq(graph,initial,goal):
    sol=[goal]
    currentP=graph[goal].parent
    while currentP!=None:
        sol.append(currentP)
        currentP=graph[currentP].parent
    sol.reverse()
    return sol        
def AStar_LabTask():
    initial='(0,0)'
    goal='(9,9)'
    graph = {
    '(0,0)': Node('(0,0)', None, [('(0,1)', 1), ('(1,0)', 1)], (0,0), 0),
    '(0,1)': Node('(0,1)', None, [('(0,0)', 1), ('(0,2)', 1), ('(1,1)', 1)], (0,1), 0),
    '(0,2)': Node('(0,2)', None, [('(0,1)', 1), ('(0,3)', 1)], (0,2), 0),
    '(0,3)': Node('(0,3)', None, [('(0,2)', 1), ('(1,3)', 1)], (0,3), 0),
    '(0,5)': Node('(0,5)', None, [('(0,6)', 1), ('(1,5)', 1)], (0,5), 0),
    '(0,6)': Node('(0,6)', None, [('(0,5)', 1), ('(0,7)', 1)], (0,6), 0),
    '(0,7)': Node('(0,7)', None, [('(0,6)', 1), ('(0,8)', 1)], (0,7), 0),
    '(0,8)': Node('(0,8)', None, [('(0,7)', 1), ('(0,9)', 1), ('(1,8)', 1)], (0,8), 0),
    '(0,9)': Node('(0,9)', None, [('(0,8)', 1), ('(1,9)', 1)], (0,9), 0),
    '(1,0)': Node('(1,0)', None, [('(0,0)', 1), ('(1,1)', 1), ('(2,0)', 1)], (1,0), 0),
    '(1,1)': Node('(1,1)', None, [('(1,0)', 1), ('(0,1)', 1), ('(2,1)', 1)], (1,1), 0),
    '(1,3)': Node('(1,3)', None, [('(0,3)', 1), ('(1,4)', 1)], (1,3), 0),
    '(1,4)': Node('(1,4)', None, [('(1,3)', 1), ('(1,5)', 1), ('(2,4)', 1)], (1,4), 0),
    '(1,5)': Node('(1,5)', None, [('(0,5)', 1), ('(1,4)', 1), ('(2,5)', 1)], (1,5), 0),
    '(1,8)': Node('(1,8)', None, [('(0,8)', 1), ('(1,9)', 1), ('(2,8)', 1)], (1,8), 0),
    '(1,9)': Node('(1,9)', None, [('(1,8)', 1), ('(0,9)', 1)], (1,9), 0),
    '(2,0)': Node('(2,0)', None, [('(1,0)', 1), ('(2,1)', 1), ('(3,0)', 1)], (2,0), 0),
    '(2,1)': Node('(2,1)', None, [('(2,0)', 1), ('(1,1)', 1), ('(2,2)', 1)], (2,1), 0),
    '(2,2)': Node('(2,2)', None, [('(2,1)', 1), ('(3,2)', 1)], (2,2), 0),
    '(2,4)': Node('(2,4)', None, [('(1,4)', 1), ('(2,5)', 1)], (2,4), 0),
    '(2,5)': Node('(2,5)', None, [('(2,4)', 1), ('(1,5)', 1), ('(3,5)', 1)], (2,5), 0),
    '(2,8)': Node('(2,8)', None, [('(1,8)', 1), ('(3,8)', 1)], (2,8), 0),
    '(3,0)': Node('(3,0)', None, [('(2,0)', 1), ('(4,0)', 1)], (3,0), 0),
    '(3,2)': Node('(3,2)', None, [('(2,2)', 1), ('(3,3)', 1)], (3,2), 0),
    '(3,3)': Node('(3,3)', None, [('(3,2)', 1), ('(4,3)',1)], (3,3), 0),
    '(3,5)': Node('(3,5)', None, [('(2,5)', 1), ('(3,6)', 1), ('(4,5)', 1)], (3,5), 0),
    '(3,6)': Node('(3,6)', None, [('(3,5)', 1), ('(3,7)', 1),('(4,6)',1)], (3,6), 0),
    '(3,7)': Node('(3,7)', None, [('(3,6)', 1), ('(4,7)', 1)], (3,7), 0),
    '(4,0)': Node('(4,0)', None, [('(3,0)', 1), ('(5,0)', 1)], (4,0), 0),
    '(4,3)': Node('(4,3)', None, [('(4,4)', 1), ('(5,3)', 1),('(3,3)',1)], (4,3), 0),
    '(4,4)': Node('(4,4)', None, [('(4,3)', 1), ('(4,5)', 1)], (4,4), 0),
    '(4,5)': Node('(4,5)', None, [('(3,5)', 1), ('(4,4)', 1),('(4,6)',1)], (4,5), 0),
    '(4,6)': Node('(4,6)', None, [('(3,6)', 1), ('(4,5)', 1),('(4,7)',1)], (4,6), 0),
    '(4,7)': Node('(4,7)', None, [('(3,7)', 1), ('(4,6)', 1),('(4,8)',1),('(5,7)',1)], (4,7), 0),
    '(4,8)': Node('(4,8)', None, [('(4,7)', 1), ('(4,9)', 1)], (4,8), 0),
    '(4,9)': Node('(4,9)', None, [('(4,8)', 1)], (4,9), 0),
    '(5,0)': Node('(5,0)', None, [('(4,0)', 1)], (5,0), 0),
    '(5,2)': Node('(5,2)', None, [('(5,3)', 1), ('(6,2)', 1)], (5,2), 0),
    '(5,3)': Node('(5,3)', None, [('(4,3)', 1), ('(5,2)', 1)], (5,3), 0),
    '(5,7)': Node('(5,7)', None, [('(4,7)', 1), ('(6,7)', 1)], (5,7), 0),
    '(6,1)': Node('(6,1)', None, [('(6,2)', 1)], (6,1), 0),
    '(6,2)': Node('(6,2)', None, [('(5,2)', 1), ('(6,1)', 1)], (6,2), 0),
    '(6,6)': Node('(6,6)', None, [('(6,7)', 1), ('(7,6)', 1)], (6,6), 0),
    '(6,7)': Node('(6,7)', None, [('(5,7)', 1), ('(6,6)', 1),('(6,8)',1),('(7,7)',1)], (6,7), 0),
    '(6,8)': Node('(6,8)', None, [('(6,7)', 1), ('(6,9)',1), ('(7,8)', 1)], (6,8), 0),
    '(6,9)': Node('(6,9)', None, [('(6,8)', 1), ('(7,9)', 1)], (6,9), 0),
    '(7,0)': Node('(7,0)', None, [('(8,0)', 1)], (7,0), 0),
    '(7,4)': Node('(7,4)', None, [('(7,5)', 1), ('(8,4)', 1)], (7,4), 0),
    '(7,5)': Node('(7,5)', None, [('(7,4)', 1), ('(7,6)', 1), ('(8,5)',1)], (7,5), 0),
    '(7,6)': Node('(7,6)', None, [('(7,5)', 1), ('(7,7)', 1), ('(6,6)',1), ('(8,6)',1)], (7,6), 0),
    '(7,7)': Node('(7,7)', None, [('(7,6)', 1), ('(7,8)', 1), ('(6,7)',1), ('(8,7)',1)], (7,7), 0),
    '(7,8)': Node('(7,8)', None, [('(7,7)', 1), ('(6,8)', 1), ('(7,9)',1), ('(8,8)',1)], (7,8), 0),
    '(7,9)': Node('(7,9)', None, [('(7,8)', 1), ('(6,9)', 1),('(8,9)',1)], (7,9), 0),
    '(8,0)': Node('(8,0)', None, [('(7,0)', 1), ('(8,1)', 1)], (8,0), 0),
    '(8,1)': Node('(8,1)', None, [('(8,0)', 1), ('(8,2)', 1), ('(9,1)',1)], (8,1), 0),
    '(8,2)': Node('(8,2)', None, [('(8,1)', 1)], (8,2), 0),
    '(8,4)': Node('(8,4)', None, [('(8,5)', 1), ('(7,4)', 1)], (8,4), 0),
    '(8,5)': Node('(8,5)', None, [('(8,4)', 1), ('(7,5)', 1), ('(8,6)',1), ('(9,5)',1)], (8,5), 0),
    '(8,6)': Node('(8,6)', None, [('(7,6)', 1), ('(8,5)', 1), ('(8,7)',1), ('(9,6)',1)], (8,6), 0),
    '(8,7)': Node('(8,7)', None, [('(8,6)', 1), ('(8,8)', 1), ('(7,7)',1), ('(9,7)',1)], (8,7), 0),
    '(8,8)': Node('(8,8)', None, [('(7,8)', 1), ('(8,7)',1), ('(8,9)', 1)], (8,8), 0),
    '(8,9)': Node('(8,9)', None, [('(8,8)', 1), ('(7,9)',1), ('(9,9)', 1)], (8,9), 0),
    '(9,1)': Node('(9,1)', None, [('(8,1)', 1)], (9,1), 0),
    '(9,5)': Node('(9,5)', None, [('(8,5)', 1), ('(9,6)',1)], (9,5), 0),
    '(9,6)': Node('(9,6)', None, [('(9,5)', 1), ('(9,7)',1), ('(8,6)',1)], (9,6), 0),
    '(9,7)': Node('(9,7)', None, [('(8,7)', 1), ('(9,6)',1)], (9,7), 0),
    '(9,9)': Node('(9,9)', None, [('(8,9)', 1)], (9,9), 0)
    }
    
    frontier=dict()
    heuristicCost=math.sqrt(((graph[goal].heuristic[0]-graph[initial].heuristic[0])**2)+((graph[goal].heuristic[1]-graph[initial].heuristic[1])**2))

    frontier[initial]=(None, heuristicCost)
    explored=dict()
    while len(frontier)!=0:
        current=findMin(frontier)
        print(current)
        del frontier[current]
        if graph[current].state==goal:
            path=actionSeq(graph,initial,goal)
            pathCost=graph[current].totalCost
            return path,pathCost
        
        heuristicCost=math.sqrt(((graph[goal].heuristic[0]-graph[current].heuristic[0])**2)+((graph[goal].heuristic[1]-graph[current].heuristic[1])**2))

        currentCost=graph[current].totalCost

        explored[current]=(graph[current].parent,heuristicCost+currentCost)

        for child in graph[current].actions:
            currentCost=child[1]+graph[current].totalCost
            heuristicCost=math.sqrt(((graph[goal].heuristic[0]-graph[child[0]].heuristic[0])**2)+((graph[goal].heuristic[1]-graph[child[0]].heuristic[1])**2))

            if child[0] in explored:
                if graph[child[0]].parent==current or child[0]==initial or explored[child[0]][1]<=currentCost+heuristicCost:
                    continue
        
            if child[0] not in frontier:
                    graph[child[0]].parent=current
                    graph[child[0]].totalCost=currentCost
                    frontier[child[0]]=(graph[child[0]].parent,currentCost+heuristicCost)
            else:
                if frontier[child[0]][1]<currentCost+heuristicCost:
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=frontier[child[0]][1]-heuristicCost
                else:
                    frontier[child[0]]=(current,currentCost+heuristicCost)
                    graph[child[0]].parent=frontier[child[0]][0]
                    graph[child[0]].totalCost=currentCost

if __name__ == "__main__":
    path, cost = AStar_LabTask()
    print("\nPath is:",path)
    print("\nTotal cost of the path is:",cost)