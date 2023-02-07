N = int(input())
A = list(map(int, input().split()))
s = 0

for ai in A:
    s += 1/ai

print(1/s)