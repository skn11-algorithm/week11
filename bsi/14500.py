# import sys
# input = sys.stdin.readline

# N, M  = map(int, input().split())
# k = []
# for i in range(N):
#     j = list(map(int, input().split()))
#     k.append(j)

# 모양을 진짜 다 지정해야한다는 생각을 못했다.
def solve():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    # 테트로미노의 모든 가능한 모양들 (상대 좌표)
    tetrominos = [
        # I 모양 (2가지)
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # 가로
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # 세로
        
        # O 모양 (1가지)
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        
        # T 모양 (4가지)
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅗ
        [(0, 1), (1, 0), (1, 1), (2, 1)],  # ㅏ
        [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅜ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅓ
        
        # S 모양 (4가지)
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # 가로 S
        [(0, 1), (1, 0), (1, 1), (2, 0)],  # 세로 S
        [(0, 1), (0, 2), (1, 0), (1, 1)],  # 가로 Z
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # 세로 Z
        
        # L 모양 (8가지)
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # ㄴ
        [(0, 0), (0, 1), (0, 2), (1, 0)],  # ㄱ
        [(0, 0), (0, 1), (1, 1), (2, 1)],  # ㄴ 뒤집음
        [(1, 0), (1, 1), (1, 2), (0, 2)],  # ㄱ 뒤집음
        [(0, 1), (1, 1), (2, 0), (2, 1)],  # ㄴ 대칭
        [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄱ 대칭
        [(0, 0), (0, 1), (1, 0), (2, 0)],  # ㄴ 대칭 뒤집음
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ 대칭 뒤집음
    ]
    
    max_sum = 0
    
    # 모든 시작 위치에서 시도
    for i in range(N):
        for j in range(M):
            # 모든 테트로미노 모양 시도
            for tetromino in tetrominos:
                current_sum = 0
                valid = True
                
                # 현재 테트로미노의 모든 칸 확인
                for di, dj in tetromino:
                    ni, nj = i + di, j + dj
                    # 범위 체크
                    if 0 <= ni < N and 0 <= nj < M:
                        current_sum += board[ni][nj]
                    else:
                        valid = False
                        break
                
                # 유효한 경우 최댓값 갱신
                if valid:
                    max_sum = max(max_sum, current_sum)
    
    return max_sum

# 메인 실행
print(solve())