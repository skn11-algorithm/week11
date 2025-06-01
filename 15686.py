import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
k = []
for i in range(N):
    j = list(map(int, input().split()))
    k.append(j)