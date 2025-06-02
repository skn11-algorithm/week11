import sys
from itertools import combinations 

input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
map=[list(map(int,input().rstrip().split())) for _ in range(N)]

homes=[ (i,j) for i in range(N) for j in range(N) if map[i][j]==1]
chickens=[ (i,j) for i in range(N) for j in range(N) if map[i][j]==2]

ans=sys.maxsize
for chicken in combinations(chickens,M):
    minimum=0
    for hx,hy in homes:
        distance=sys.maxsize
        for cx,cy in chicken:
            tmp=(abs(hx-cx)+abs(hy-cy))
            distance=min(distance,tmp)
        minimum+=distance
    ans=min(ans,minimum)

print(ans)
