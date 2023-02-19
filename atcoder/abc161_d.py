from collections import deque

K = int(input())
Q = deque(list(range(1, 10)))
cnt = 0

while Q:
    cnt += 1
    n = Q.popleft()
    if cnt == K:
        print(n)
        exit()
    l = n % 10
    if l > 0: Q.append(n*10+l-1)
    Q.append(n*10+l)
    if l < 9: Q.append(n*10+l+1)
