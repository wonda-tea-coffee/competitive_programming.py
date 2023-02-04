import string
N, X = map(int, (input().split()))
s = ""
for a in list(string.ascii_uppercase):
    s += a * N
print(s[X-1])
