N, M = map(int, input().split())
ans = []
A = set(map(int, input().split()))
B = set(map(int, input().split()))
for ai in A:
    if not ai in B:
        ans.append(ai)
for bi in B:
    if not bi in A:
        ans.append(bi)

print(*sorted(ans))