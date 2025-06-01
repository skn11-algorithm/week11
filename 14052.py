from collections import deque
from itertools import combinations

def bfs(vgraph,vrs):
    copy_vrs = deque(vrs)
    visited = [[False]*m for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for x,y in copy_vrs:
        visited[x][y] = True

    while copy_vrs:
        x,y = copy_vrs.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m: #빈공간 바이러스 전파
                if visited[nx][ny] == False and vgraph[nx][ny] == 0:
                    vgraph[nx][ny] = 2
                    visited[nx][ny] = True
                    copy_vrs.append((nx,ny))
    return vgraph

n,m = map(int,input().split())
graph = []
empty = []
vrs = deque()
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 2: #바이러스면 바이러스 큐에 넣음
            vrs.append((i,j))
        if arr[j] == 0: #빈 칸이면 empty 배열에 저장 -> 조합 완탐
            empty.append((i,j))

    graph.append(arr)

safe = 0
for a,b,c in combinations(empty, 3):
    #graph를 vgraph에 복사
    vgraph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            vgraph[i][j] = graph[i][j]
    for x,y in [a,b,c]: #벽 3개 치기
        vgraph[x][y] = 1

    vgraph = bfs(vgraph,vrs)
    zero = 0
    for i in vgraph:
        for j in i:
            if j==0:
                zero += 1
    safe = max(safe, zero)
print(safe)