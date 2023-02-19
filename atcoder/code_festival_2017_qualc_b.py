N = int(input())
A = list(map(int, input().split()))
b = 1
for ai in A:
    if ai % 2 == 0:
        b *= 2
print(3**N - b)