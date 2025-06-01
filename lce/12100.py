import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0

def move(board, direction):
    new_board = [[0]*n for _ in range(n)]
    
    for i in range(n):
        temp = []
        for j in range(n):
            if direction == 0:     # 왼쪽
                val = board[i][j]
            elif direction == 1:   # 오른쪽
                val = board[i][n - 1 - j]
            elif direction == 2:   # 위
                val = board[j][i]
            else:                  # 아래
                val = board[n - 1 - j][i]
            
            if val != 0:
                temp.append(val)
        
        merged = []
        idx = 0
        while idx < len(temp):
            if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
                merged.append(temp[idx] * 2)
                idx += 2
            else:
                merged.append(temp[idx])
                idx += 1
        merged += [0] * (n - len(merged))
        
        for j in range(n):
            if direction == 0:
                new_board[i][j] = merged[j]
            elif direction == 1:
                new_board[i][n - 1 - j] = merged[j]
            elif direction == 2:
                new_board[j][i] = merged[j]
            else:
                new_board[n - 1 - j][i] = merged[j]
    
    return new_board

def dfs(board, depth):
    global res
    res = max(res, max(map(max, board)))
    if depth == 5:
        return
    for d in range(4):
        next_board = move(copy.deepcopy(board), d)
        if next_board != board:  # 가지치기: 변화가 있을 때만 진행
            dfs(next_board, depth + 1)

dfs(board, 0)
print(res)
