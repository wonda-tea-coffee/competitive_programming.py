N = int(input())
if len(set(map(int, input().split()))) == N:
    print("YES")
else:
    print("NO")