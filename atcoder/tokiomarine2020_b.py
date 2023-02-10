A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V*T - abs(B-A) >= W*T:
    print("YES")
else:
    print("NO")