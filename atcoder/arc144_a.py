N = int(input())
if N % 4 > 0:
    ans = [str(N%4)]
else:
    ans = []
ans += ["4"] * (N//4)

print(2*N)
print("".join(ans))