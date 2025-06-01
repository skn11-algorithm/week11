# import sys
# input = sys.stdin.readline

# N = int(input())
# schedule = {}
# for i in range(N):
#     a = list(map(int, input().split()))
#     schedule[i] = a

# add_P = []

# def count(add, i):
#     if i < N-1:
#         add += schedule[i][1]
#         return count(add, i + schedule[i][0])

#     else:
#         return add
    

# for i in schedule:
#     add = 0
#     add = count(add, i)
#     add_P.append(add)
#     a = 0

# print(max(add_P))


import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])