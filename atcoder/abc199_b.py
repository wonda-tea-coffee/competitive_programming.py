N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = max(A)
r = min(B)
print(max(0, r-l+1))