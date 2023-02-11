def sum_of_divisors(n):
    i = 1
    divisors = set()
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    return len(divisors)

X, Y = map(lambda x: sum_of_divisors(int(x)), input().split())

if X > Y:
    print("X")
elif X < Y:
    print("Y")
else:
    print("Z")
