def solve(n):
    # print(n)
    if len(n) == 1:
        m = int(n)
        return m*(m+1)//2

    ret = 0
    head = int(n[0])
    l = len(n)-1
    for i in range(head):
        ret += i * 10**l + 45*l*10**(l-1)
    ret += head*(int(n[1:])+1)
    return ret + solve(n[1:])

print(solve(input()))
