# 퇴사
n = int(input())

days = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    if i + days[i][0] <= n:
        dp[i] = max(days[i][1] + dp[i+days[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])