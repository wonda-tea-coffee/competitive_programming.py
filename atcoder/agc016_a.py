import string

s = input()

def solve(s, c):
    ret = 0
    while len(set(s)) > 1:
        ret += 1
        t = []
        for i in range(len(s)-1):
            if s[i] == c or s[i+1] == c:
                t.append(c)
            else:
                t.append(s[i])
        s = "".join(t)

    return ret

ans = 10**10
for c in string.ascii_lowercase:
    ans = min(ans, solve(s, c))
print(ans)
