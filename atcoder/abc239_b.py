from decimal import Decimal, getcontext, ROUND_FLOOR

c = getcontext()
c.rounding = ROUND_FLOOR
d = Decimal(int(input())) / Decimal(10)
print(d.quantize(Decimal('0')))
