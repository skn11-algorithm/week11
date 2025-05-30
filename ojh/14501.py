import sys

# 목표 : 퇴사일 전 상담의 이익(Pi)을 최대화

input=sys.stdin.readline
N=int(input().rstrip())

schedule=[] # 일별 [상담소요기간, 비용] 저장
dp=[-1]*(N+1) # 요일별 최대 이익 저장

for _ in range(N):
    schedule.append(list(map(int,input().rstrip().split())))

schedule=[[0,0]]+schedule

def func(day):
    if day>N:
        return 0
    
    if dp[day]!=-1:
        return dp[day]
    
    Ti,Pi=schedule[day]
    
    if day + Ti -1 > N : # 상담 못하니까
        dp[day]=func(day+1) # 다음날로 넘어감

    else:
        take=Pi+func(day+Ti) # 오늘 상담
        skip=func(day+1) # 오늘 상담 안 함
        dp[day]=max(take,skip) # 더 큰 이익 저장
    
    return dp[day]

# 재귀 일어남
# func(1)
# ├── func(4)      # 상담한 경우: 1일 + 3일 상담(Ti=3)
# │   ├── func(5)
# │   │   ├── func(7)
# │   │   │   ├── func(9) ...
# ├── func(2)      # 상담 안 하고 다음 날로 넘어감
# │   ├── func(7)


print(func(1))