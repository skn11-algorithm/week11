from collections import deque
import sys

# 벨트를 회전시키고 로봇 위치도 회전
def rotate_belt():
    belt.appendleft(belt.pop())  # 벨트 회전
    visited.appendleft(visited.pop())  # 로봇 위치도 회전
    visited[n-1] = False  # 내리는 위치의 로봇 제거

# 로봇을 한 칸씩 이동
def move_robot():
    for i in range(n-2, -1, -1):  # 끝에서부터 순차적으로 체크
        if visited[i] and not visited[i+1] and belt[i+1] > 0:
            visited[i], visited[i+1] = False, True  # 로봇 이동
            belt[i+1] -= 1  # 이동한 칸의 내구도 감소
    visited[n-1] = False  # 내리는 위치는 항상 비워줘야 함

# 로봇을 첫 칸에 올림
def load_robot():
    if belt[0] > 0:
        visited[0] = True
        belt[0] -= 1

# 내구도가 0인 칸의 개수가 k 이상이면 종료
def check_end():
    return belt.count(0) < k

# 입력 처리
n, k = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))
visited = deque([False] * (2 * n))  # 로봇이 있는지 여부
level = 0

# 시뮬레이션 시작
while True:
    level += 1
    rotate_belt()
    move_robot()
    load_robot()
    if not check_end():
        break

print(level)
