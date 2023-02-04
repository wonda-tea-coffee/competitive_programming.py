from decimal import Decimal, getcontext, ROUND_HALF_UP

A, B = map(int, input().split())

c = getcontext()
c.rounding = ROUND_HALF_UP
d = Decimal(B/A)
print(d.quantize(Decimal('.001')))
