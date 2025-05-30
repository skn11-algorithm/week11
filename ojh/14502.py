import sys,copy
from collections import deque
from itertools import combinations

input=sys.stdin.readline
N,M=map(int,(input().rstrip().split())) # 세로(행), 가로(열)

graph=[list(map(int,(input().rstrip().split()))) for _ in range(N)]

# 빈칸 / 바이러스 위치
empty=[(i,j) for i in range(N) for j in range(M) if graph[i][j]==0]
virus=[(i,j) for i in range(N) for j in range(M) if graph[i][j]==2]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# 바이러스 전파
def bfs(graph):
    queue=deque(virus)

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                graph[nx][ny]=2
                queue.append((nx,ny))
    
    return sum(row.count(0) for row in graph)

# 조합에 따라 벽 3개 고정한 맵 만들고
# → 바이러스 bfs로 퍼뜨리기 
# → 안전구역 계산
# 반복

max_safe=0
for walls in combinations(empty,3):
    graph_copy=copy.deepcopy(graph)
    for x,y in walls:
        graph_copy[x][y]=1
    max_safe=max(max_safe,bfs(graph_copy))

print(max_safe)
    