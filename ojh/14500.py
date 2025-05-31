import sys

input=sys.stdin.readline

N,M = map(int,input().rstrip().split()) # 세로(행), 가로(열)
arr=[list(map(int,input().rstrip().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

ans=0 # 최댓값 저장

# 테트로미노 : 깊이 4 탐색으로 만들 수 있음 ( 'ㅜ' 모양 제외 )
def dfs(x,y,depth,maximum):
    global ans
    if depth==3:
        ans=max(ans,maximum)
        return

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny]=True # 방문처리 
            dfs(nx,ny,depth+1,maximum+arr[nx][ny])
            # 재귀 다녀오면 다른 경로 탐색을 위해 방문 해제 
            visited[nx][ny]=False

    
# 'ㅜ' 모양 : 중심점에서 4방향 탐색
# 4방향 가능하면 가장 작은 값 빼기
# 3방향 가능하면 그냥 다 더하기
# 2방향 이하면 'ㅜ' 모양 아님 -> 무시

def func(x,y):
    global ans
    possible=[]
    maximum=arr[x][y]

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            possible.append(arr[nx][ny])
    
    length=len(possible)
    if length==4:
        possible.sort()
        maximum+=sum(possible[1:])
    elif length==3:
        maximum+=sum(possible)
    else :
        return
    ans=max(ans,maximum)
    return
    
for i in range(N):
    for j in range(M):
        visited[i][j]=True # 자기 자신 재방문 방지
        dfs(i,j,0,arr[i][j])
        visited[i][j]=False 
        # 방문 처리를 해제하지 않으면 다음 시작점이 해당 칸을 다시 시작점으로 못 씀
        
        func(i,j)

print(ans)