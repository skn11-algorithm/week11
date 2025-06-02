import sys

input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
robot=[False]*(2*N)
cnt=0

while True:
    cnt+=1

    #1. 회전
    arr=[arr[-1]]+arr[:-1]
    robot=[False]+robot[:-1]

    # 로봇 내리기
    if robot[N-1]:
        robot[N-1]=False
    
    # 앞에 있는 로봇이 먼저 움직이면, 뒤에 있던 로봇이 "덮어쓰기" 당함
    # 뒤부터 순회
    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and arr[i+1]>0:
            robot[i+1]=True
            robot[i]=False
            arr[i+1]-=1

    #3. 로봇 올리기
    if arr[0]>0:
        if not robot[0]:
            arr[0]-=1
            robot[0]=True
    

    if arr.count(0)>=K:
        break

print(cnt)


    



