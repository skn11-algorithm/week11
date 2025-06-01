# 퇴사

# 입력
# - 상담의 개수: n
# - 상담 기간 ti, 상담 보수 pi

# 출력
# - 백준이가 얻을 수 있는 최대 이익

# 풀이 아이디어
# - 우선순위 큐를 사용하자 (백준의 강의실 배정 문제와 비슷한거같음?!) -> 4프로에서 틀림
# - (상담 보수, 상담 기간)를 큐에 저장하고, 상담 보수, 상담 기간 순으로 정렬

import heapq
import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n+1)

for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    if i + time[i] <= n:
        dp[i + time[i]] = max(dp[i+time[i]], dp[i]+pay[i])
            
print(dp[n])