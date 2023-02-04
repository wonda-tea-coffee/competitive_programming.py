N = int(input())
f, a = 0, 0
for _ in range(N):
    s = input()
    if s == "For":
        f += 1
    else:
        a += 1

if f >= a:
    print("Yes")
else:
    print("No")
