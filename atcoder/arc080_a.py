N = int(input())
a = list(map(int, input().split()))
oddcnt = 0
cnt2 = 0
cnt4 = 0
for ai in a:
    m = ai % 4
    if m == 1 or m == 3:
        oddcnt += 1
    elif m == 2:
        cnt2 += 1
    else:
        cnt4 += 1

if oddcnt > cnt4 + 1:
    print("No")
elif oddcnt == cnt4 + 1:
    if cnt2 > 0:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")
