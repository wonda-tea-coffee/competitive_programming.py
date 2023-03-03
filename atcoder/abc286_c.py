def rotate(s):
    return s[1:] + s[0]

def calc(s):
    ret = 0
    for i in range(N//2):
        if s[i] != s[-i-1]:
            ret += 1
    return ret

N, A, B = map(int, input().split())
S = input()

if len(S) == 1:
    print(0)
    exit()

ans = N*max(A, B)
for i in range(N):
    ans = min(ans, A*i + B*calc(S))
    S = rotate(S)
print(ans)
