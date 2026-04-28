def dfs_maze_all_paths():
    maze=[
        ['S',0,0],
        [1,0,1],
        [0,0,'E']
    ]
    paths=[]
    def backtrack(x,y,path):
        path.append((x,y))
        if (x,y)==(2,2):
            paths.append(path[:])
            path.pop()
            return
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx
            ny=y+dy
            if (0<=nx<3 and 0<=ny<3 and maze[nx][ny]!=1 and (nx,ny) not in path):
                backtrack(nx,ny,path)
        path.pop()
    backtrack(0,0,[])
    return paths

all_paths = dfs_maze_all_paths()
print("Total solutions:", len(all_paths), "\n")

for i,path in enumerate(all_paths,1):
    print(f"Path {i} ({len(path)-1} moves):")
    for pos in path:
        print(pos,end="->")
