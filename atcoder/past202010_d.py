N = int(input())
S = input()

l = 0
li = 0
while li < N and S[li] == ".":
    l += 1
    li += 1
r = 0
ri = N-1
while ri >= 0 and S[ri] == ".":
    ri -= 1
    r += 1

d = "."
m = 0
# print(l, r)
# print(S[l:N-r])
while S[l:N+r].count(d) > 0:
    d += "."
    m += 1

# print(m)
while l + r < m:
    l += 1

print(l, r)
