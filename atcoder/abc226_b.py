N = int(input())
s = set()
for _ in range(N):
    L, *a = map(int, input().split())
    s.add(tuple(a))
print(len(s))