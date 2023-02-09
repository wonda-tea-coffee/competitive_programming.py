import sys

N = int(input())
for x in range(1, N+1):
    if int(x * 1.08) == N:
        print(x)
        sys.exit(0)

print(":(")
