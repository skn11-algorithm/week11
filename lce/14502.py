from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def spread(new_lab):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and 0 <= ny < m and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2
                q.append((nx, ny))
    return sum(row.count(0) for row in new_lab)

res = 0
for walls in combinations(empty, 3):
    new_lab = copy.deepcopy(lab)
    for x, y in walls:
        new_lab[x][y] = 1
    res = max(res, spread(new_lab))

print(res)