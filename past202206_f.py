H, W = map(int, input().split())
S = [None] * H

for i in range(H):
    S[i] = list(map(int, input().split()))

N = int(input())
for i in range(N):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if S[r][c] == 0:
        continue

    S[r][c] = 0
    while True:
        count = 0

        for hi in range(max(H-2, 0), -1, -1):
            if S[hi][c] > 0 and S[hi+1][c] == 0:
                count += 1
                S[hi+1][c], S[hi][c] = S[hi][c], S[hi+1][c]

        if count == 0:
            break

for hi in range(H):
    print(' '.join(list(map(str, S[hi]))))
