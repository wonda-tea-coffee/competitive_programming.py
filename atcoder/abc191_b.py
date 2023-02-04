N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for ai in A:
    if ai != X:
        B.append(ai)
print(*B)