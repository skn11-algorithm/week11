import sys
input = sys.stdin.readline

# DFS 함수: 테트로미노 4칸을 탐색하면서 최대 합 계산
def DFS(L, total, x, y):
    global maximum

    # 가지치기 (남은 칸이 모두 max_val일 때의 최댓값보다 작으면 중단)
    if maximum >= total + max_val * (4 - L):
        return

    # 블록 4칸을 모두 선택했으면 결과 갱신
    if L == 4:
        maximum = max(total, maximum)
        return
    else:
        for i in range(4):  # 상우하좌
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visit[xx][yy] == 0:
                # 'ㅗ' 모양 처리: 2번째 칸일 때 한 번 더 현재 좌표 기준으로 탐색
                if L == 2:
                    visit[xx][yy] = 1
                    DFS(L + 1, total + a[xx][yy], x, y)
                    visit[xx][yy] = 0

                # 일반 DFS 탐색
                visit[xx][yy] = 1
                DFS(L + 1, total + a[xx][yy], xx, yy)
                visit[xx][yy] = 0

# 입력
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]  # 격자판
visit = [[0] * m for _ in range(n)]  # 방문 체크

maximum = 0  # 결과 저장
max_val = max(map(max, a))  # 격자 내 최대값 (가지치기에 사용)

# 방향벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 좌표에서 DFS 시작
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        DFS(1, a[i][j], i, j)
        visit[i][j] = 0

print(maximum)
