from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([False]*n)
step = 0

while True:
    step += 1
    a.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and a[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            a[i+1] -= 1
    robot[-1] = False

    if a[0] > 0:
        robot[0] = True
        a[0] -= 1

    if a.count(0) >= k:
        break

print(step)