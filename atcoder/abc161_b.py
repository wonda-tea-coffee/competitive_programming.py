N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A) / (4*M)
l = len(list(filter(lambda x: x >= s, A)))
if l >= M:
    print("Yes")
else:
    print("No")
