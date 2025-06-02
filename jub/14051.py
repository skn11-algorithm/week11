#DP문제
# 뒤쪽 인덱스 부터 접근
# i 일에 상담을 진행한 경우/ 아닌 경우로 나눠서 최댓값을 구하자
# i 일에 상담한 경우 = P[i] + dp[i+Ti]
# i 일에 상담하지 않은 경우 = dp[i+1]

import sys
read = sys.stdin.readline

N=int(read().strip())
T,P = [0],[0]
for i in range (1,N+1):
    t,p = map(int,read().split())
    T.append(t)
    P.append(p)

dp = [0]*(N+6)
for i in range(N,0,-1):
    if i+T[i]>N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])
print(dp[1])
