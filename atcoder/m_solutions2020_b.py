A, B, C = map(int, input().split())
K = int(input())
# A < B < C
c = 0
while A >= B:
    B *= 2
    c += 1
while B >= C:
    C *= 2
    c += 1

if c <= K:
    print("Yes")
else:
    print("No")