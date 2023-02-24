S, C = map(int, input().split())
s1 = min(S, C//2)
S -= s1
C -= s1*2
if S > 0:
    print(s1)
else:
    print(s1 + C//4)
