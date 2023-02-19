def is_palindrome(s):
    return s == "".join(reversed(s))

A, B = map(int, input().split())
ans = 0
for i in range(A, B+1):
    if is_palindrome(str(i)):
        ans += 1
print(ans)
