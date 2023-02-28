N = int(input())
a = list(map(int, input().split()))
D = [0]
for ai in a:
    D.append(D[-1] + ai)
ans = float("inf")
for i in range(N-1):
    ans = min(ans, abs(D[i+1] - (D[N] - D[i+1])))
print(ans)
