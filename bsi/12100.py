# import sys
# input = sys.stdin.readline

# N = int(input())
# k = []
# for i in range(N):
#     j = list(map(int, input().split()))
#     k.append(j)

# # 최적의 값을 찾는 로직?
# # 숫자를 어디에서 생성시키는 것인지 : 무작위긴 하지만, 최대값을 얻을 수 있는 최적의 위치가 정해져 있다 가정

import copy

def solve():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    # 왼쪽으로 이동
    def move_left(board):
        new_board = copy.deepcopy(board)
        for i in range(N):
            # 0이 아닌 숫자들만 모으기
            row = [x for x in new_board[i] if x != 0]
            
            # 합치기
            merged = []
            j = 0
            while j < len(row):
                if j + 1 < len(row) and row[j] == row[j + 1]:
                    # 같은 수가 인접해 있으면 합치기
                    merged.append(row[j] * 2)
                    j += 2  # 두 칸 건너뛰기
                else:
                    merged.append(row[j])
                    j += 1
            
            # 나머지를 0으로 채우기
            merged.extend([0] * (N - len(merged)))
            new_board[i] = merged
        
        return new_board
    
    # 오른쪽으로 이동
    def move_right(board):
        new_board = copy.deepcopy(board)
        for i in range(N):
            # 행을 뒤집고, 왼쪽 이동 적용 후, 다시 뒤집기
            new_board[i] = new_board[i][::-1]
        
        new_board = move_left(new_board)
        
        for i in range(N):
            new_board[i] = new_board[i][::-1]
        
        return new_board
    
    # 위로 이동
    def move_up(board):
        # 전치 -> 왼쪽 이동 -> 다시 전치
        new_board = copy.deepcopy(board)
        
        # 전치 (행과 열 바꾸기)
        transposed = [[new_board[j][i] for j in range(N)] for i in range(N)]
        
        # 왼쪽 이동 적용
        moved = move_left(transposed)
        
        # 다시 전치
        result = [[moved[j][i] for j in range(N)] for i in range(N)]
        
        return result
    
    # 아래로 이동
    def move_down(board):
        # 전치 -> 오른쪽 이동 -> 다시 전치
        new_board = copy.deepcopy(board)
        
        # 전치
        transposed = [[new_board[j][i] for j in range(N)] for i in range(N)]
        
        # 오른쪽 이동 적용
        moved = move_right(transposed)
        
        # 다시 전치
        result = [[moved[j][i] for j in range(N)] for i in range(N)]
        
        return result
    
    # 보드에서 최대값 찾기
    def get_max_value(board):
        max_val = 0
        for i in range(N):
            for j in range(N):
                max_val = max(max_val, board[i][j])
        return max_val
    
    # DFS로 모든 경우 탐색
    def dfs(board, moves_left):
        if moves_left == 0:
            return get_max_value(board)
        
        max_result = 0
        
        # 4방향 모두 시도
        for move_func in [move_left, move_right, move_up, move_down]:
            new_board = move_func(board)
            result = dfs(new_board, moves_left - 1)
            max_result = max(max_result, result)
        
        return max_result
    
    return dfs(board, 5)

# 메인 실행
print(solve())