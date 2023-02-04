from decimal import Decimal, getcontext, ROUND_HALF_UP

c = getcontext()
c.rounding = ROUND_HALF_UP
d = Decimal(input())
print(d.quantize(Decimal('0')))
