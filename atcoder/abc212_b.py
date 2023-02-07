import sys

s = input()
if len(set(s)) == 1:
    print("Weak")
    sys.exit(0)

s = list(map(int, list(s)))
for i in range(3):
    if (s[i]+1)%10 != s[i+1]:
        print("Strong")
        sys.exit(0)

print("Weak")
