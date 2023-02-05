A, B, C, D, E, F, X = map(int, input().split())

t = (X//(A+C)*A + min(X%(A+C), A)) * B
a = (X//(D+F)*D + min(X%(D+F), D)) * E

if t < a:
    print("Aoki")
elif t > a:
    print("Takahashi")
else:
    print("Draw")