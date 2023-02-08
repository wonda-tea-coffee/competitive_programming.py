def is_palindrome(s):
    return s == "".join(reversed(s))

def check(s):
    if not is_palindrome(s): return False

    m = len(s)//2
    return is_palindrome(s[:m]) and is_palindrome(s[m+1:])

S = input()
if check(S):
    print("Yes")
else:
    print("No")
