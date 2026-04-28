class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def get_path(graph, goal):
    path = []
    curr = goal
    while curr:
        path.append(curr)
        curr = graph[curr].parent
    path.reverse()
    return path

def dfs_8puzzle():
    start = ((1,2,3),(4,0,5),(6,7,8))
    goal  = ((1,2,3),(4,5,6),(7,8,0))
    
    graph = {start: Node(start)}
    frontier = [start]
    explored = set()
    
    while frontier:
        cur = frontier.pop()           # DFS
        
        if cur in explored:
            continue
        explored.add(cur)
        
        if cur == goal:
            return get_path(graph, cur)
        
        # Find blank tile (0)
        for i in range(3):
            for j in range(3):
                if cur[i][j] == 0:
                    x, y = i, j
        
        # Try all 4 moves
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in cur]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_tuple = tuple(tuple(row) for row in new_state)
                
                if new_tuple not in explored:
                    graph[new_tuple] = Node(new_tuple, cur)
                    frontier.append(new_tuple)
    
    return None

# ============= Run Task 1 =============
result = dfs_8puzzle()

if result:
    print("Solution Found! Full Path:\n")
    for step, state in enumerate(result):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print("-" * 20)
    print(f"Total steps: {len(result)-1}")
else:
    print("No solution found")