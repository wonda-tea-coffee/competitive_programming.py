def is_leap(y):
    if y % 400 == 0: return True
    if y % 100 == 0: return False
    return y % 4 == 0

if is_leap(int(input())):
    print("YES")
else:
    print("NO")