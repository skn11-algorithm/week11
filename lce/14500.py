n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
res = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]

def dfs(x, y, depth, total):
    global res
    if depth == 4:
        res = max(res, total)
        return
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total + board[nx][ny])
            visited[nx][ny] = False

def check_extra(x, y):
    global res
    for shape in [
        [(0,0), (0,1), (0,2), (1,1)],
        [(0,0), (1,0), (2,0), (1,1)],
        [(0,0), (1,-1), (1,0), (1,1)],
        [(0,1), (1,0), (1,1), (2,1)]
    ]:
        try:
            total = 0
            for dx, dy in shape:
                nx, ny = x+dx, y+dy
                if nx < 0 or ny < 0: raise IndexError
                total += board[nx][ny]
            res = max(res, total)
        except:
            continue

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra(i, j)

print(res)