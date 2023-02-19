N, A, B = map(int, input().split())
ans = N // (A + B) * A
N %= (A + B)

if N >= A:
    print(ans + A)
else:
    print(ans + N)
