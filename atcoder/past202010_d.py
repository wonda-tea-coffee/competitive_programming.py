N = int(input())
S = input()

li = 0
lc = 0
while S[li] == ".":
    li += 1
    lc += 1

ri = N-1
rc = 0
while S[ri] == ".":
    ri -= 1
    rc += 1

mid = 0
while li <= ri:
    c = 0
    while li <= ri and S[li] == ".":
        li += 1
        c += 1
    mid = max(mid, c)
    li += 1

while lc + rc < mid:
    lc += 1

print(lc, rc)
