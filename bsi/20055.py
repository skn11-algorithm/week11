def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 로봇의 위치를 추적 (True면 로봇이 있음, False면 없음)
    robots = [False] * N
    step = 0
    
    while True:
        step += 1
        
        # 1단계: 벨트가 한 칸 회전
        # 내구도 배열을 회전 (시계방향)
        A = [A[-1]] + A[:-1]
        
        # 로봇도 함께 회전
        robots = [False] + robots[:-1]
        
        # 내리는 위치(N-1 인덱스)에 로봇이 있으면 즉시 내림
        if robots[N-1]:
            robots[N-1] = False
        
        # 2단계: 로봇이 이동
        # 뒤에서부터 확인해야 앞의 로봇이 뒤의 로봇을 밀어내지 않음
        for i in range(N-2, -1, -1):  # N-2부터 0까지
            if robots[i]:  # 현재 위치에 로봇이 있고
                next_pos = i + 1
                # 다음 위치에 로봇이 없고, 내구도가 1 이상이면 이동
                if not robots[next_pos] and A[next_pos] > 0:
                    robots[i] = False
                    robots[next_pos] = True
                    A[next_pos] -= 1  # 내구도 감소
        
        # 내리는 위치에 로봇이 있으면 즉시 내림 (이동 후 재확인)
        if robots[N-1]:
            robots[N-1] = False
        
        # 3단계: 올리는 위치에 로봇을 올림
        # 올리는 위치(0번 인덱스)에 로봇이 없고 내구도가 1 이상이면
        if not robots[0] and A[0] > 0:
            robots[0] = True
            A[0] -= 1  # 내구도 감소
        
        # 4단계: 내구도가 0인 칸의 개수가 K개 이상이면 종료
        zero_count = A.count(0)
        if zero_count >= K:
            break
    
    return step

# 메인 실행
print(solve())