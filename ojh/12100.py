import sys,copy

def up(board):
    for j in range(N):
        cursor=0 # 이동시킬 위치
        for i in range(1,N):
            if board[i][j]!=0 : # 0이면 이동시킬 이유X
                tmp=board[i][j]
                board[i][j]=0

                if board[cursor][j]==0:
                    board[cursor][j]=tmp    

                elif board[cursor][j]==tmp:
                    board[cursor][j]=tmp*2
                    cursor+=1
                
                elif board[cursor][j]!=tmp:
                    cursor+=1
                    board[cursor][j]=tmp 
    return board

def down(board):
    for j in range(N):
        cursor=N-1 # 이동시킬 위치
        for i in range(N-2,-1,-1):
            if board[i][j]!=0 : # 0이면 이동시킬 이유X
                tmp=board[i][j]
                board[i][j]=0

                if board[cursor][j]==0:
                    board[cursor][j]=tmp    

                elif board[cursor][j]==tmp:
                    board[cursor][j]=tmp*2
                    cursor-=1
                
                elif board[cursor][j]!=tmp:
                    cursor-=1
                    board[cursor][j]=tmp 
    return board

def left(board):
    for i in range(N):
        cursor=0 # 이동시킬 위치
        for j in range(1,N):
            if board[i][j]!=0 : # 0이면 이동시킬 이유X
                tmp=board[i][j]
                board[i][j]=0

                if board[i][cursor]==0:
                    board[i][cursor]=tmp    

                elif board[i][cursor]==tmp:
                    board[i][cursor]=tmp*2
                    cursor+=1
                
                elif board[i][cursor]!=tmp:
                    cursor+=1
                    board[i][cursor]=tmp 
    return board

def right(board):
    for i in range(N):
        cursor=N-1 # 이동시킬 위치
        for j in range(N-2,-1,-1):
            if board[i][j]!=0 : # 0이면 이동시킬 이유X
                tmp=board[i][j]
                board[i][j]=0

                if board[i][cursor]==0:
                    board[i][cursor]=tmp    

                elif board[i][cursor]==tmp:
                    board[i][cursor]=tmp*2
                    cursor-=1
                
                elif board[i][cursor]!=tmp:
                    cursor-=1
                    board[i][cursor]=tmp 
    return board

def backtrack(board,depth):
    global ans

    if depth==5:
        for i in range(N):
            for j in range(N):
                if board[i][j]>ans:
                    ans=board[i][j]
        return
    
    for i in range(4):
        board_copy=copy.deepcopy(board)
        if i==0:
            backtrack(up(board_copy),depth+1)
        elif i==1:
            backtrack(down(board_copy),depth+1)
        elif i==2:
            backtrack(left(board_copy),depth+1)
        else:
            backtrack(right(board_copy),depth+1)

input=sys.stdin.readline
N=int(input())

board=[list(map(int,input().rstrip().split())) for _ in range(N)]
depth=1
ans=0
backtrack(board,0)
print(ans)

