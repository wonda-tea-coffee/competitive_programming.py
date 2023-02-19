def check(s):
    if s[0] != "A": return False
    if s[2:-1].count("C") != 1: return False
    cnt = 0
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            cnt += 1
    return cnt == len(s)-2

if check(input()):
    print("AC")
else:
    print("WA")